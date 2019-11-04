#!/usr/bin/env python
import rospy
from common_msgs.msg import SelfMadeMessage

rospy.init_node('message_publisher', anonymous=True)


msg = SelfMadeMessage()

pub = rospy.Publisher("DateTime_msg", SelfMadeMessage, queue_size = 1)
rate = rospy.Rate(1)
msg.number.data = 0
msg.rotation.orientation.x = 0.0
msg.rotation.orientation.y = 0.0
msg.rotation.orientation.z = 0.0
msg.rotation.orientation.w = 0.0
msg.rotation.position.x = 0.0
msg.rotation.position.y = 0.0
msg.rotation.position.z = 0.0

while not rospy.is_shutdown():
    msg.number.data += 1
    msg.rotation.orientation.x += 1
    msg.rotation.orientation.y += 0.01
    msg.rotation.orientation.z += 0.05
    msg.rotation.orientation.w += 0.005
    msg.rotation.position.x += 1
    msg.rotation.position.y += 2
    msg.rotation.position.z += 3
    pub.publish(msg)
    print(msg.number)
    print(msg.rotation)
    rate.sleep()
    
