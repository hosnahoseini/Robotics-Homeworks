#!/usr/bin/python3
import math
# ROS
import rospy
from geometry_msgs.msg import Twist
from turtlebot3_object_tracker.srv import DetectionService, DetectionServiceRequest

class Controller:
    def __init__(self) -> None:
        # Use these Twists to control your robot
        self.move = Twist()
        self.move.linear.x = 0.1
        self.freeze = Twist()

        # The "p" parameter for your p-controller, TODO: you need to tune this
        self.angular_vel_coef = 1

        # Create a service proxy for your human detection service
        rospy.wait_for_service('detection_service')
        self.detection_service_proxy = rospy.ServiceProxy('detection_service', DetectionService)

        # Create a publisher for your robot "cmd_vel"
        self.cmd_vel_publisher = rospy.Publisher('/follower/cmd_vel', Twist, queue_size=1)

    def run(self) -> None:
        try:
            while not rospy.is_shutdown():
                # Call your service to detect humans
                detection_service_response = self.call_detection_service()
                
                # If humans are detected, adjust the robot's movement
                if detection_service_response.detection_info:
                    self.adjust_robot_movement(detection_service_response)
                else:
                    # If no humans are detected, freeze the robot
                    self.cmd_vel_publisher.publish(self.freeze)
                    rospy.loginfo("freeze")

                rospy.sleep(0.1)

        except rospy.exceptions.ROSInterruptException:
            pass

    def call_detection_service(self):
        try:
            # Create a detection service request
            request = DetectionServiceRequest()
            request.label = "person"

            # Call the detection service
            response = self.detection_service_proxy(request)
            
            # Return the detection info
            return response

        except rospy.ServiceException as e:
            rospy.logerr("Service call failed: %s" % str(e))

    def adjust_robot_movement(self, detection_service_response):
        # TODO: Implement your control logic here
        # You can use the detection_service_response (e.g., position, bounding box) to adjust the robot's movement
        # For example, you can calculate the desired angular velocity based on the detected position

        # Calculate the desired angular velocity based on the detected position
        error = self.calculate_error(detection_service_response)

        rospy.loginfo(error)
        rospy.loginfo('=' * 10)

        angular_vel = self.angular_vel_coef * error

        # Set the robot's movement with the calculated angular velocity
        self.move.angular.z = angular_vel

        # Publish the robot's movement
        self.cmd_vel_publisher.publish(self.move)

    def calculate_error(self, detection_service_response):
        # Extract the bounding box coordinates
        upper_left = detection_service_response.detection_info[0]
        lower_right = detection_service_response.detection_info[1]

        # Extract the image size
        image_size = detection_service_response.image_size
        image_width = image_size[1]

        # Calculate the center point of the bounding box
        center_x = (upper_left.x + lower_right.x) / 2

        # Calculate the desired position as the center of the image
        desired_position = image_width / 2

        # Calculate the error as the difference between the detected position and the desired position
        error = desired_position - center_x

        # Calculate the angle between the robot and the center of the human bounding box
        angle = math.atan2(error, image_width)  # Angle in radians

        return angle


if __name__ == "__main__":
    rospy.init_node("controller", anonymous=True)
    
    controller = Controller()
    controller.run()
