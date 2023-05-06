#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import cv2
import numpy as np

class DroneController:
    def __init__(self):
        rospy.init_node("drone_controller", anonymous=True)
        self.bridge = CvBridge()
        self.image_sub = rospy.Subscriber("/webcam/image_raw", Image, self.kameraCallback)

    def kameraCallback(self, data):
        try:
            cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
        except CvBridgeError as e:
            print(e)
        x1, y1, x2, y2 = 0, 319, 639, 479
        roi = cv_image[y1:y2, x1:x2]

        gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray, (5, 5), 0)

        ret, thresh = cv2.threshold(blur, 200, 255, cv2.THRESH_BINARY)
        contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        center_x = cv_image.shape[1] / 2
        min_distance = float("inf")
        best_contour = None
        for contour in contours:
            M = cv2.moments(contour)
            if M["m00"] != 0:
                cx = int(M["m10"] / M["m00"])
                cy = int(M["m01"] / M["m00"])
                distance = abs(cx - center_x)
                if distance < min_distance:
                    min_distance = distance
                    best_contour = contour

        if best_contour is not None:
            # Calculate the centroid of the best contour
            M = cv2.moments(best_contour)
            if M["m00"] != 0:
                cx = int(M["m10"] / M["m00"])
                cy = int(M["m01"] / M["m00"])

                image_center_x = cv_image.shape[1] / 2
                yaw = (cx - image_center_x) * 0.01
                velocity = 1

                # Draw the contour on the region of interest (ROI)
                cv2.drawContours(roi, [best_contour], 0, (0, 255, 0), 2)

        cv2.imshow("Image", cv_image)
        cv2.waitKey(1)

    def run(self):
        rospy.spin()

if __name__ == '__main__':
    controller = DroneController()
    controller.run()
