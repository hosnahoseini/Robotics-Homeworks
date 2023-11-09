#!/usr/bin/env python3

from nav_msgs.msg import Odometry
import tf
import rospy
from geometry_msgs.msg import Twist
import math

class ControllerNode:

    def __init__(self):
        rospy.init_node('pid_controller')
        self.cmd_vel_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
        
        # Initialize ROS subscriber for robot odometry
        rospy.Subscriber('/odom', Odometry, self.odometry_callback)
        self.num_destinations = 4 # Set the number of destinations here

        rospy.on_shutdown(self.shutdown)

        self.target_x = 10
        self.target_y = 0
        self.target_yaw = 0
        self.current_x = 0
        self.current_y = 0
        self.current_yaw = 0
        self.Kp = 0.1  # Proportional gain
        self.Ki = 0.01 # Integral gain
        self.Kd = 10 # Derivative gain
        self.integral_x = 0.0
        self.integral_yaw = 0.0
        self.previous_error_x = 0.0
        self.previous_error_yaw = 0.0
        self.dt = 0.005
        self.move_threshold = 0.25
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
        proportional_x = self.Kp * error_x
        proportional_yaw = 3 * self.Kp * error_yaw

        # Integral terms
        self.integral_x += error_x * self.dt
        self.integral_yaw += error_yaw * self.dt
        integral_x = self.Ki * self.integral_x
        integral_yaw = self.Ki * self.integral_yaw

        # Derivative terms
        derivative_x = self.Kd * (error_x - self.previous_error_x) / self.dt
        derivative_yaw = 2 * self.Kd * (error_yaw - self.previous_error_yaw) / self.dt

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
        rate = rospy.Rate(1/self.dt)  
        while not rospy.is_shutdown():
            x, yaw = self.calculate_control_command()
            twist = Twist()
            twist.linear.x = x
            twist.angular.z = yaw
            self.cmd_vel_pub.publish(twist)
            distance_to_dest = math.sqrt((self.target_x - self.current_x) ** 2 + (self.target_y - self.current_y) ** 2)

            if distance_to_dest < self.move_threshold:
                return
            rate.sleep()


    
if __name__ == "__main__":
    controller = ControllerNode()