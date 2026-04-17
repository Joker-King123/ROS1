#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from std_msgs.msg import String

def talker():
    # 初始化ROS节点，节点名为'talker'
    rospy.init_node('talker', anonymous=True)
    
    # 创建一个Publisher，发布到'hello_topic'话题，消息类型为String
    pub = rospy.Publisher('hello_topic', String, queue_size=10)
    
    # 设置发布频率为1Hz
    rate = rospy.Rate(1)
    
    count = 0
    while not rospy.is_shutdown():
        # 准备要发布的消息
        hello_str = "Hello World! %s" % rospy.get_time()
        
        # 发布消息
        pub.publish(hello_str)
        
        # 在终端打印消息
        rospy.loginfo("已发送: %s", hello_str)
        
        # 等待1秒
        rate.sleep()
        count += 1

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
