#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from std_msgs.msg import String

def callback(data):
    # 当收到消息时的回调函数
    rospy.loginfo("已收到: %s", data.data)

def listener():
    # 初始化ROS节点，节点名为'listener'
    rospy.init_node('listener', anonymous=True)
    
    # 创建一个Subscriber，订阅'hello_topic'话题
    rospy.Subscriber('hello_topic', String, callback)
    
    # 保持程序运行直到节点被关闭
    rospy.spin()

if __name__ == '__main__':
    listener()
