cmake_minimum_required(VERSION 2.8.3)
project(common_msgs)

find_package(catkin REQUIRED COMPONENTS
    rospy
    std_msgs
    geometry_msgs
    message_generation
)


add_message_files(
  FILES
  SelfMadeMessage.msg
)    

add_service_files(
  FILES
  SelfMadeService.srv
)

generate_messages(
  DEPENDENCIES
  geometry_msgs
  std_msgs
)
    

catkin_package(
  CATKIN_DEPENDS geometry_msgs rospy std_msgs
)



