#!/usr/bin/env python3
import rospy
from std_msgs.msg import Time
from geometry_msgs.msg import Quaternion
from common_msgs.msg import SelfMadeMessage


def callback(msg):
    msg.current_time = rospy.get_rostime()
    second = msg.current_time.secs
    msg.rotation = Quaternion(x = second//3600, y = second // 60, z = second, w = second // 86400)

rospy.init_node("message_subscriber")
sub = rospy.Subscriber("DateTime_msg", SelfMadeMessage, callback)
rospyl.spin()
