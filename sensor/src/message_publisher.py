#!/usr/bin/env python3
import rospy
from common_msgs.msg import SelfMadeMessage

rospy.init_node('message_publisher', anonymous=True)


msg = SelfMadeMessage

pub = rospy.Publisher("DateTime_msg", SelfMadeMessage, queue_size = 1)
rate = rospy.Rate(1)

while not rospy.is_shutdown():
    pub.publish(msg)
    print("published")
    rate.sleep()
    
    
