#!/usr/bin/env python3

from nav_msgs.msg import Odometry
import tf
import rospy
from next_destination.srv import GetNextDestination, GetNextDestinationRequest
from geometry_msgs.msg import Twist
import math
import numpy as np

class ControllerNode:

    def __init__(self, shape):
        rospy.init_node('controller_node')
        self.cmd_vel_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
        self.get_next_destination_service = rospy.ServiceProxy('get_next_destination', GetNextDestination)
        
        # Initialize ROS subscriber for robot odometry
        rospy.Subscriber('/odom', Odometry, self.odometry_callback)
        rospy.on_shutdown(self.shutdown)

        self.target_x = 0
        self.target_y = 0
        self.target_yaw = 0

        # gains for angular PID controller
        self.Kp_ang = 2.6
        self.Ki_ang = 0.001
        self.Kd_ang = 0.9

        # gains for linear PID controller
        self.Kp_lin = 0.75
        self.Ki_lin = 0.001
        self.Kd_lin = 2.5


        self.epsilon = 0.2
        self.integral_x = 0.0
        self.integral_yaw = 0.0
        self.previous_error_x = 0.0
        self.previous_error_yaw = 0.0
        self.dt = 0.05
        self.previous_index = 0
        self.back_point = False

        if shape == 0:
            # rectangle

            X1 = np.linspace(-3, 3, 100)
            Y1 = np.array([2] * 100)

            Y2 = np.linspace(2, -2, 100)
            X2 = np.array([3] * 100)

            X3 = np.linspace(3, -3, 100)
            Y3 = np.array([-2] * 100)

            Y4 = np.linspace(-2, 2, 100)
            X4 = np.array([-3] * 100)

            self.X = np.concatenate([X1, X2, X3, X4])
            self.Y = np.concatenate([Y1, Y2, Y3, Y4])
        elif shape == 1:
            # Star

            X1 = np.linspace(0, 3 , 100)
            Y1 = - (7/3) * X1  + 12

            X2 = np.linspace(3, 10 , 100)
            Y2 = np.array([5]*100)

            X3 = np.linspace(10, 4 , 100)
            Y3 = (5/6) * X3  - (10/3)

            X4 = np.linspace(4, 7 , 100)
            Y4 = -(3) * X4  + 12

            X5 = np.linspace(7, 0 , 100)
            Y5 = -(4/7) * X5  - 5

            X6 = np.linspace(0, -7 , 100)
            Y6 = (4/7) * X6  - 5

            X7 = np.linspace(-7, -4 , 100)
            Y7 = 3 * X7  + 12

            X8 = np.linspace(-4, -10 , 100)
            Y8 = -(5/6) * X8  - (10/3)

            X9 = np.linspace(-10, -3 , 100)
            Y9 = np.array([5]*100)

            X10 = np.linspace(-3, 0 , 100)
            Y10 = (7/3) * X10  + 12

            self.X = np.concatenate([X1,X2,X3,X4,X5,X6,X7,X8,X9,X10])
            self.Y = np.concatenate([Y1,Y2,Y3,Y4,Y5,Y6,Y7,Y8,Y9,Y10])

        elif shape == 2:
            # Logarithmic spiral 

            a = 0.17
            k = math.tan(a)
            X , Y = [] , []

            for i in range(150):
                t = i / 20 * math.pi
                dx = a * math.exp(k * t) * math.cos(t)
                dy = a * math.exp(k * t) * math.sin(t)
                X.append(dx)
                Y.append(dy) 
            self.X = X
            self.Y = Y

        self.run()

    def calculate_control_command(self, linear_err, angular_err):
        # Calculate the errors
        error_x = linear_err
        error_yaw = angular_err

        # Proportional terms
        proportional_x = self.Kp_lin * error_x
        proportional_yaw = self.Kp_ang * error_yaw

        # Integral terms
        self.integral_x += error_x * self.dt
        self.integral_yaw += error_yaw * self.dt
        integral_x = self.Ki_lin * self.integral_x
        integral_yaw = self.Ki_ang * self.integral_yaw

        # Derivative terms
        derivative_x = self.Kd_lin * (error_x - self.previous_error_x) / self.dt
        derivative_yaw = self.Kd_ang * (error_yaw - self.previous_error_yaw) / self.dt

        # Calculate the control commands
        control_command_x = proportional_x + integral_x + derivative_x
        control_command_yaw = proportional_yaw + integral_yaw + derivative_yaw

        # Update the previous errors
        self.previous_error_x = error_x
        self.previous_error_yaw = error_yaw

        return control_command_x, control_command_yaw

    def odometry_callback(self, msg):
        # Get robot's current position
        self.current_x = msg.pose.pose.position.x
        self.current_y = msg.pose.pose.position.y
        orientation = msg.pose.pose.orientation
        _, _, self.current_yaw = tf.transformations.euler_from_quaternion((orientation.x, orientation.y, orientation.z, orientation.w))

    def shutdown(self):
        rospy.loginfo('Stopping the robot')
        self.cmd_vel_pub.publish(Twist())
        rospy.sleep(1)

    def euclidean_distance(self, x1, x2, y1, y2):
        point1 = np.array((x1, y1))
        point2 = np.array((x2, y2))
        return np.linalg.norm(point1 - point2)

    def next_destination(self):
        my_min = 99999
        my_x = 0
        my_y = 0
        min_index = -1

        for i in range(len(self.X)):
            diff_ang = float("{:.2f}".format(np.arctan2((self.Y[i] - self.current_y), (self.X[i] - self.current_x))))
            if self.current_yaw > 0:
                sign = -1 if (self.current_yaw - math.pi < diff_ang < self.current_yaw) else +1
            else:
                sign = +1 if (self.current_yaw + math.pi > diff_ang > self.current_yaw) else -1
            diff_ang = sign * (math.pi - abs(abs(self.current_yaw - diff_ang) - math.pi))
            if -math.pi / 2 < diff_ang < math.pi / 2:
                my_distance = self.euclidean_distance(self.current_x, self.X[i], self.current_y, self.Y[i])
                if my_min > my_distance and my_distance > abs(self.epsilon):
                    my_min = my_distance
                    min_index = i
                    my_x = self.X[i]
                    my_y = self.Y[i]
        
        # no point is on the front, so find nearest point on the back
        if min_index == -1:
            for i in range(len(self.X)):
                diff_ang = float("{:.2f}".format(np.arctan2((self.Y[i] - self.current_y), (self.X[i] - self.current_x))))
                if self.current_yaw > 0:
                    sign = -1 if (self.current_yaw - math.pi < diff_ang < self.current_yaw) else +1
                else:
                    sign = +1 if (self.current_yaw + math.pi > diff_ang > self.current_yaw) else -1
                diff_ang = sign * (math.pi - abs(abs(self.current_yaw - diff_ang) - math.pi))
                my_distance = self.euclidean_distance(self.current_x, self.X[i], self.current_y, self.Y[i])
                if my_min > my_distance and my_distance > abs(self.epsilon):
                    # don't go on the previous line
                    if diff_ang > 0.1:
                        my_min = my_distance
                        min_index = i
                        my_x = self.X[i]
                        my_y = self.Y[i]


        self.target_x = my_x
        self.target_y = my_y
        rospy.loginfo(f"{self.target_x}, {self.target_y}")
        self.goal_orientation = float("{:.2f}".format(np.arctan2((self.target_y - self.current_y), (self.target_x - self.current_x))))


    def run(self):
        rospy.sleep(1)
        rate = rospy.Rate(1/self.dt)  

        while not rospy.is_shutdown():
            self.next_destination()
            
            linear_err = self.euclidean_distance(self.current_x, self.target_x, self.current_y, self.target_y)
            if self.current_yaw > 0:
                sign = -1 if (self.current_yaw - math.pi < self.goal_orientation < self.current_yaw) else +1
            else:
                sign = +1 if (self.current_yaw + math.pi > self.goal_orientation > self.current_yaw) else -1
            angular_err = sign * (math.pi - abs(abs(self.current_yaw - self.goal_orientation) - math.pi))

            x, yaw = self.calculate_control_command(linear_err, angular_err)
            twist = Twist()
            twist.linear.x = x
            twist.angular.z = yaw
            self.cmd_vel_pub.publish(twist)
            rate.sleep() 
            



    
if __name__ == "__main__":
    
    controller = ControllerNode(shape=2)
