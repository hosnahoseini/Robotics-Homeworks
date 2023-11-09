#!/usr/bin/env python3

from nav_msgs.msg import Odometry
import tf
import rospy
from next_destination.srv import GetNextDestination, GetNextDestinationRequest
from geometry_msgs.msg import Twist
import math

class ControllerNode:

    def __init__(self):
        rospy.init_node('controller_node')
        self.cmd_vel_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
        self.get_next_destination_service = rospy.ServiceProxy('get_next_destination', GetNextDestination)
        
        # Initialize ROS subscriber for robot odometry
        rospy.Subscriber('/odom', Odometry, self.odometry_callback)
        self.num_destinations = 3 # Set the number of destinations here

        rospy.on_shutdown(self.shutdown)

        self.target_x = 0
        self.target_y = 0
        self.target_yaw = 0

        # gains for angular PID controller
        self.Kp_ang = 0.1
        self.Ki_ang = 0.001
        self.Kd_ang = 1

        # gains for linear PID controller
        self.Kp_lin = 0.1
        self.Ki_lin = 0.001
        self.Kd_lin = 1


        self.integral_x = 0.0
        self.integral_yaw = 0.0
        self.previous_error_x = 0.0
        self.previous_error_yaw = 0.0
        self.dt = 0.005
        self.move_threshold = 0.2
        self.run()

    def calculate_control_command(self):
        # Calculate the errors
        error_x = abs(self.target_x - self.current_x)

        # Calculate the angle between the current position and target position
        target_yaw = math.atan2(self.target_y - self.current_y, self.target_x - self.current_x)

        # Adjust the target_yaw to be within -pi to pi range
        error_yaw = abs(target_yaw - self.current_yaw)

        # rospy.loginfo(f'{error_x}, {error_yaw}')

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


    def run(self):
        rospy.sleep(1)
        self.destination_counter = 0
        while self.destination_counter < self.num_destinations:
            self.target_x, self.target_y = self.get_next_destination()
            distance_to_dest = math.sqrt((self.target_x - self.current_x) ** 2 + (self.target_y - self.current_y) ** 2)
            rate = rospy.Rate(1/self.dt)  
            rospy.loginfo(f'({self.target_x}, {self.target_y })')

            while distance_to_dest > self.move_threshold:
                x, yaw = self.calculate_control_command()
                # rospy.loginfo(f'({x}, {yaw})')
                twist = Twist()
                twist.linear.x = x
                twist.angular.z = yaw
                self.cmd_vel_pub.publish(twist)
                rate.sleep()    
                distance_to_dest = math.sqrt((self.target_x - self.current_x) ** 2 + (self.target_y - self.current_y) ** 2)


            self.destination_counter += 1

    def get_next_destination(self):
        req = GetNextDestinationRequest()
        req.current_x = self.current_x
        req.current_y = self.current_y
        res = self.get_next_destination_service(req)
        rospy.loginfo(f"Next destination: ({res.next_x}, {res.next_y})")

        return res.next_x, res.next_y

    def publish_twist(self, linear, angular):
        twist = Twist()
        twist.linear.x = linear
        twist.angular.z = angular
        self.cmd_vel_pub.publish(twist)
    
if __name__ == "__main__":
    controller = ControllerNode()