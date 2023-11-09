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
        self.move_vel = rospy.get_param('~move_vel') # Get move velocity from launch file
        self.angular_speed = 0.1
        self.cmd_vel_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
        self.get_next_destination_service = rospy.ServiceProxy('get_next_destination', GetNextDestination)
        # Initialize ROS subscriber for robot odometry
        rospy.Subscriber('/odom', Odometry, self.odometry_callback)
        self.rotate_threshold = 0.02 # Set rotation threshold here
        self.move_threshold = 0.2 # Set move threshold here
        self.current_x = 0.0 # set your desired initial x position here
        self.current_y = 0.0 # set your desired initial y position here
        self.num_destinations = 5 # Set the number of destinations here
        self.destination_counter = 0 # Counter to keep track of the number of destinations reached
        self.errors = []
        self.run()
        
    def run(self):
        rospy.sleep(1)
        while self.destination_counter < self.num_destinations:
            next_x, next_y = self.get_next_destination()
            self.rotate_to_destination(next_x, next_y)
            self.move_to_destination(next_x, next_y)
            self.destination_counter += 1
        rospy.loginfo("mean of erros:")
        mean_of_err = sum(self.errors) / self.num_destinations
        rospy.loginfo(mean_of_err)

    def get_next_destination(self):
        req = GetNextDestinationRequest()
        req.current_x = self.current_x
        req.current_y = self.current_y
        res = self.get_next_destination_service(req)
        rospy.loginfo(f"Next destination: ({res.next_x}, {res.next_y})")

        return res.next_x, res.next_y

    def rotate_to_destination(self, dest_x, dest_y):
        while True:
            angle_to_dest = math.atan2(dest_y - self.current_y, dest_x - self.current_x)

            if abs(angle_to_dest - self.get_robot_yaw()) < self.rotate_threshold:
                rospy.loginfo(math.degrees(angle_to_dest - self.get_robot_yaw()))
                self.cmd_vel_pub.publish(Twist())
                rospy.sleep(2)
                rospy.loginfo(math.degrees(self.get_robot_yaw()))

                
                break
            else:
                self.publish_twist(0, self.angular_speed)

        rospy.loginfo('Rotation to destination completed.')

    def move_to_destination(self, dest_x, dest_y):
        previous_distance = 1000

        self.publish_twist(0, 0)

        while True:

            distance_to_dest = math.sqrt((dest_x - self.current_x) ** 2 + (dest_y - self.current_y) ** 2)

            if distance_to_dest < self.move_threshold or previous_distance < distance_to_dest:
                self.publish_twist(0, 0)
                self.errors.append(distance_to_dest)
                rospy.sleep(1)                    
                break
            else:
                self.publish_twist(self.move_vel, 0)
                previous_distance = distance_to_dest
                rospy.sleep(0.2)
            
        rospy.loginfo('Movement to destination completed.')

    def odometry_callback(self, msg):
        # Update current position from odometry
        self.current_x = msg.pose.pose.position.x
        self.current_y = msg.pose.pose.position.y

    def publish_twist(self, linear, angular):
        twist = Twist()
        twist.linear.x = linear
        twist.angular.z = angular
        self.cmd_vel_pub.publish(twist)
    
    def get_robot_yaw(self):
        # Wait for the most recent message from the odom topic
        msg = rospy.wait_for_message("/odom", Odometry)

        # Extract the robot's yaw angle from the orientation quaternion
        orientation = msg.pose.pose.orientation
        roll, pitch, yaw = tf.transformations.euler_from_quaternion((orientation.x, orientation.y, orientation.z, orientation.w))
        
        return yaw
    
if __name__ == "__main__":
    controller = ControllerNode()