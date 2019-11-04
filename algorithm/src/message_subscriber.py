#!/usr/bin/env python
import rospy
from common_msgs.msg import SelfMadeMessage


def callback(msg):
    print("subscribed")
    print(msg.number.data * msg.rotation.position.x)
    print(msg.rotation.orientation.x * msg.rotation.position.y)
    print("----------")
    
rospy.init_node("message_subscriber")
sub = rospy.Subscriber("DateTime_msg", SelfMadeMessage, callback)
rospy.spin()
