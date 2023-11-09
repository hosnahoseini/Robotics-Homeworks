#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import LaserScan
from std_msgs.msg import Float32, Float64
from obstacle_detect.msg import ClosetObstacle # add this line
import math

closest_obstacle_pub = None

def laserCallback(scan):
    closest_range = scan.range_max
    closest_index = -1

    # iterate through the laser scan data to find the closest obstacle
    arr = scan.ranges

    
    for i in range(len(arr)):
        range_ = scan.ranges[i]

        # ignore invalid ranges
        if math.isnan(range_) or range_ < scan.range_min or range_ > scan.range_max:
            continue

        # update closest range_ and index
        if range_ < closest_range:
            closest_range = range_
            closest_index = i

    # publish closest obstacle specifications on ClosestObstacle topic
    if closest_index != -1:
        closest_angle = scan.angle_min + closest_index * scan.angle_increment
        closest_obstacle_msg = ClosetObstacle() # create message instance
        closest_obstacle_msg.distance = closest_range # set distance field
        closest_obstacle_msg.direction = closest_angle # set direction field
        closest_obstacle_pub.publish(closest_obstacle_msg) # publish message

def main():
    global closest_obstacle_pub
    rospy.init_node('sensor_node')

    # subscribe to the LaserScan topic
    rospy.Subscriber('scan', LaserScan, laserCallback)

    # advertise the ClosestObstacle topic with custom message type
    closest_obstacle_pub = rospy.Publisher('ClosestObstacle', ClosetObstacle, queue_size=10)

    rospy.spin()

if __name__ == '__main__':
    main()
