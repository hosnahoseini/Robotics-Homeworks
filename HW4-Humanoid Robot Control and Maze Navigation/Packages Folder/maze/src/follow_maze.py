#!/usr/bin/python3

import math
import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

class PIDController():


    def __init__(self):
        
        rospy.init_node('maze_follower_node', anonymous=True)
        
        self.Ki = 0
        self.Kp = 0.9
        self.Kd = 15
        
        self.dt = 0.005
        self.v = 0.3
        self.D = 0.7
        rate = 1/self.dt
        
        self.r = rospy.Rate(rate)
        self.cmd_vel = rospy.Publisher('/cmd_vel', Twist, queue_size=5)
        self.errs = []


    def distance_from_wall(self):
        laser_data = rospy.wait_for_message("/scan" , LaserScan)
        rng = laser_data.ranges[:180]
        d = min(rng)
        return d

    
    def follow_wall(self):
        
        d = self.distance_from_wall()    
        integral = 0
        prev_error = 0
        
        move_cmd = Twist()
        move_cmd.angular.z = 0
        move_cmd.linear.x = self.v

        while not rospy.is_shutdown():
            self.cmd_vel.publish(move_cmd)

            err = d - self.D
            integral += err * self.dt
            
            P = self.Kp * err
            I = self.Ki * integral
            D = self.Kd * (err - prev_error)

            move_cmd.angular.z = P + I + D

            if abs(move_cmd.angular.z) > math.radians(30):
                move_cmd.linear.x = self.v / 4
            else:
                move_cmd.linear.x = self.v
            prev_error = err         
            
            rospy.loginfo(f"error : {err} speed : {move_cmd.linear.x} theta : {move_cmd.angular.z}")
            
            d = self.distance_from_wall()

            self.r.sleep()
            

if __name__ == '__main__':
    try:
        pidc = PIDController()
        pidc.follow_wall()
    except rospy.ROSInterruptException:
        rospy.loginfo("Navigation terminated.")