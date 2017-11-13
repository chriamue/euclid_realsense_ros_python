#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Example Python node to publish on a specific topic.
"""

# Import required Python code.
from __future__ import print_function
import sys

import roslib
import rospy
import cv2
from matplotlib import pyplot as plt

from std_msgs.msg import String
from sensor_msgs.msg import Image
from sensor_msgs.msg import CompressedImage
from cv_bridge import CvBridge, CvBridgeError



class EuclidRS(object):
    '''
    Node example class.
    '''
    def __init__(self):
        self.bridge = CvBridge()
        #self.image_sub = rospy.Subscriber("/camera/color/image_raw", Image, self.imageCallback)
        self.depthImage_sub = rospy.Subscriber("/camera/depth/image_raw", Image, self.depthImageCallback)
        plt.ion()

    def imageCallback(self, data):
        try:
          cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
        except CvBridgeError as e:
          print(e)
        cv2.imshow("Image window", cv_image)
        cv2.waitKey(3)

    def depthImageCallback(self, depthData):
        try:
          cv_depthimage = self.bridge.imgmsg_to_cv2(depthData, "16UC1")
        except CvBridgeError as e:
          print(e)
        cv2.imshow("Depth Image window", cv_depthimage)
        cv2.waitKey(3)

def main(args):
  ers = EuclidRS()
  rospy.init_node('euclid_rs', anonymous=True)
  try:
    rospy.spin()
  except KeyboardInterrupt:
    print("Shutting down")
  cv2.destroyAllWindows()
 
if __name__ == '__main__':
  main(sys.argv)