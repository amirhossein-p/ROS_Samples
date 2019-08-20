cmake_minimum_required(VERSION 2.8.3)
project(PubSub)

find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  std_msgs
  message_generation
)

add_message_files(
   FILES
   sensor.msg
)

catkin_package(

)

include_directories(
  ${catkin_INCLUDE_DIRS}
)

