#!/usr/bin/python3

import random
import rospy
from std_msgs.msg import String
from hw0.msg import proximity

def talker():
    pub = rospy.Publisher("distance", proximity, queue_size=10)
    rospy.init_node("sensor", anonymous=True)
    rate = rospy.Rate(0.2) # Hz (number per second)

    while not rospy.is_shutdown():
        msg = proximity()
        msg.up = random.randint(10, 200)
        msg.down = random.randint(10, 200)
        msg.left = random.randint(10, 200)
        msg.right = random.randint(10, 200)

        rospy.loginfo(msg)
        pub.publish(msg)
        rate.sleep()


if __name__ == "__main__":
    talker()
    