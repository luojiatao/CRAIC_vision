#!/usr/bin/env python3
# coding:utf-8 
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

def callback(data):
    bridge = CvBridge()
    # 将ROS图像消息转换为OpenCV图像格式
    cv_image = bridge.imgmsg_to_cv2(data, desired_encoding='bgr8')
    # 保存图像到指定路径
    cv2.imwrite("/path/to/save/image.jpg", cv_image)
    rospy.loginfo("Image saved successfully!")

def main():
    rospy.init_node('image_listener', anonymous=True)
    # 订阅/cam话题
    rospy.Subscriber("/cam", Image, callback)
    # 保持程序运行直到被关闭
    rospy.spin()

if __name__ == '__main__':
    main()
