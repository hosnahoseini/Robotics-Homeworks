#!/usr/bin/env python3
import rospy
from std_msgs.msg import String
from hw0.msg import proximity, twist

state = 0
def callback(data):
    global state
    degree = 0
    clockwise = True
    distances = [data.up, data.right, data.down, data.left]
    min_dis_dir = min(range(len(distances)), key=lambda x : distances[x])
    if (min_dis_dir != state):
        diff = min_dis_dir - state

        if (diff == 1 or state == -3):  # turn right 90 degree
            degree = 90
            clockwise = True
        elif (diff == -1 or diff == 3): # turn left 90 degree
            degree = 90
            clockwise = False
        elif(diff == 2 or diff == -2):  # turn 180 degree
            degree = 180
            clockwise = True

    msg = twist()
    msg.degree = degree
    msg.clockwise = clockwise

    pub1 = rospy.Publisher("motor1", twist, queue_size=10)
    pub2 = rospy.Publisher("motor2", twist, queue_size=10)

    pub1.publish(msg)
    pub2.publish(msg)

    rospy.loginfo(msg)
    state = min_dis_dir


def listener():
    rospy.init_node('controller', anonymous=True)

    rospy.Subscriber("distance", proximity, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()
   
if __name__ == '__main__':
       listener()