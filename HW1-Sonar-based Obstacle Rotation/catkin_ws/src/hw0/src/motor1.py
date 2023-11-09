#!/usr/bin/python3

import rospy
from hw0.msg import twist

def callback(data):
    clockwise = 'clock wise' if data.clockwise else 'counter clock wise'
    rospy.loginfo(data.degree)
    rospy.loginfo(clockwise)


def listener():
    rospy.init_node('motor1', anonymous=True)
    rospy.Subscriber("motor1", twist, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()


if __name__ == "__main__":
    listener()