#!/usr/bin/env python3
import rospy
import random
import math
from next_destination.srv import GetNextDestination, GetNextDestinationResponse 

def callback(req):
    # rospy.loginfo(req)

    while True:
        # Generate random coordinates between -5 and 5
        x = random.randint(-5, 5)
        y = random.randint(-5, 5)

        # Calculate the distance between the generated coordinates and the current coordinate
        distance = math.sqrt((x - req.current_x) ** 2 + (y - req.current_y) ** 2)

        # If the distance is greater than or equal to 5, return the coordinates
        if distance >= 1:
            break

    res = GetNextDestinationResponse()
    res.next_x = x
    res.next_y = y

    # rospy.loginfo(res)

    return res

def listener():

    rospy.init_node('mission_node', anonymous=True)
    s = rospy.Service('/get_next_destination', GetNextDestination, callback)
    rospy.spin()

if __name__ == "__main__":
    listener()

