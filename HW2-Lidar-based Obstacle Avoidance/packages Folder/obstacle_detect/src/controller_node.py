#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from obstacle_detect.msg import ClosetObstacle
import math

forward_speed = 0.2 # m/s
angular_speed = 0.5 # rad/s
min_distance = 2.0 # meters

closest_obstacle = None

def closestObstacleCallback(msg):
    global closest_obstacle
    closest_obstacle = msg

def moveRobot():
    global closest_obstacle
    rospy.init_node('controller_node')

    # subscribe to ClosestObstacle topic
    rospy.Subscriber('ClosestObstacle', ClosetObstacle, closestObstacleCallback)

    # create Twist message publisher
    vel_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    vel_msg = Twist()

    # set initial velocity
    vel_msg.linear.x = forward_speed
    vel_msg.angular.z = 0.0
    state = 'GO'
    while not rospy.is_shutdown():

        # if there is no obstacle, continue moving forward
        if closest_obstacle is None:
            vel_msg.linear.x = forward_speed
            vel_msg.angular.z = 0.0
            rospy.loginfo("there is no obstacle, continue moving forward")
        # if the obstacle is too close, stop moving forward and turn away from the obstacle
        elif closest_obstacle.distance < min_distance and (abs(closest_obstacle.direction) <= math.pi/2 or abs(closest_obstacle.direction) >= 3 * math.pi / 2):
            vel_msg.linear.x = 0.0
            vel_msg.angular.z = angular_speed if closest_obstacle.direction > 0 else -angular_speed
            rospy.loginfo("the obstacle is too close turn away from the obstacle")
        # if the obstacle is behind the robot, start moving forward again
        else:
            vel_msg.linear.x = forward_speed
            vel_msg.angular.z = 0.0
            rospy.loginfo("the obstacle is behind the robot or too far, start moving forward again")
            
        # publish the velocity message
        vel_pub.publish(vel_msg)

        # sleep for a short duration to avoid flooding the publisher
        rospy.sleep(0.1)

if __name__ == '__main__':
    try:
        moveRobot()
    except rospy.ROSInterruptException:
        pass
