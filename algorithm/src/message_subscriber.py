#!/usr/bin/env python
import rospy
from common_msgs.msg import SelfMadeMessage
from common_msgs.srv import SelfMadeService, SelfMadeServiceResponse

count = 0

def service_callback(request):
    response = SelfMadeServiceResponse(result = request.type1 and request.type2)
    print("--------10 seconds passed----------")
    return response

def callback(msg):
    print("subscribed")
    cal1 = msg.number.data * msg.rotation.position.x
    cal2 = msg.rotation.orientation.x * msg.rotation.position.y
    print(cal1)
    print(cal2)
    print("----------")
    
rospy.init_node("message_subscriber")
sub = rospy.Subscriber("DateTime_msg", SelfMadeMessage, callback)
service = rospy.Service('reset', SelfMadeService, service_callback)
rospy.spin()

