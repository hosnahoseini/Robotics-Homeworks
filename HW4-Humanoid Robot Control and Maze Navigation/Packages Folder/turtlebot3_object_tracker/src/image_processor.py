#!/usr/bin/python3

# Python
import copy

# Object detection
import cv2
import numpy as np
from ultralytics import YOLO
from ultralytics.yolo.utils.plotting import Annotator
from ultralytics.yolo.engine.results import Results

# ROS
import rospy
from sensor_msgs.msg import Image
from turtlebot3_object_tracker.srv import DetectionService, DetectionServiceResponse
from geometry_msgs.msg import Point

class ImageProcessor:
    def __init__(self) -> None:
        # Image message
        self.image_msg = Image()

        self.image_res = 240, 320, 3  # Camera resolution: height, width
        self.image_np = np.zeros(self.image_res)  # The numpy array to pour the image data into

        # TODO: Subscribe to your robot's camera topic
        # NOTE: Make sure you use the provided listener for this subscription
        self.camera_subscriber = rospy.Subscriber('/follower/camera/image', Image, self.camera_listener)

        # TODO: Instantiate your YOLO object detector/classifier model
        self.model = YOLO()  # Instantiate your YOLO model here

        self.cv2_frame_size = 400, 320
        cv2.namedWindow("robot_view", cv2.WINDOW_NORMAL)
        cv2.resizeWindow("robot_view", *self.cv2_frame_size)

        # Setup the "human detection" service
        self.human_detection_service = rospy.Service('detection_service', DetectionService, self.detection_service_callback)

        self.update_view()

    def camera_listener(self, msg: Image):
        self.image_msg.data = copy.deepcopy(msg.data)

    def detection_service_callback(self, req):
        label = req.label

        # Perform object detection on the current image frame
        self.results = self.model(self.image_np)
        
        # Extract the detection information and image size
        detection_info = []
        
        for result in self.results:
            # rospy.loginfo(result)
            detection_count = result.boxes.shape[0]
            # rospy.loginfo(detection_count)

            for i in range(detection_count):
                cls = int(result.boxes.cls[i].item())
                name = result.names[cls]
                
                if name == label:
                    confidence = float(result.boxes.conf[i].item())
                    bounding_box = result.boxes.xyxy[i].cpu().numpy()
                    p1 = Point()
                    p2 = Point()
                    p1.x = int(bounding_box[0])
                    p1.y = int(bounding_box[1])
                    p2.x = int(bounding_box[2])
                    p2.y = int(bounding_box[3])

                    # rospy.loginfo(f'{bounding_box[0]}, {bounding_box[1]}, {bounding_box[2]}, {bounding_box[3]}')
                    detection_info.append(p1)
                    detection_info.append(p2)


        image_size = [self.image_res[0], self.image_res[1]]

        # Create the response message
        response = DetectionServiceResponse()
        response.detection_info = detection_info
        response.image_size = image_size

        return response

    def update_view(self):
        try:
            while not rospy.is_shutdown():
                if len(self.image_msg.data) == 0:
                    continue

                self.image_np = np.frombuffer(self.image_msg.data, dtype=np.uint8)
                self.image_np = self.image_np.reshape(self.image_res)

                frame = copy.deepcopy(self.image_np)

                # Convert the frame to an image
                image = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

                # Use the annotator to draw object bounding boxes on the image
                annotator = Annotator(im=image)
                image_with_boxes = annotator.result()

                # Show the image with bounding boxes
                cv2.imshow("robot_view", image_with_boxes)
                cv2.waitKey(1)

        except rospy.exceptions.ROSInterruptException:
            pass


if __name__ == "__main__":
    rospy.init_node("image_processor", anonymous=True)

    rospy.on_shutdown(cv2.destroyAllWindows)

    image_processor = ImageProcessor()

    rospy.spin()
