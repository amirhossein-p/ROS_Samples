cmake_minimum_required(VERSION 2.8.3)
project(PubSubMsg)

find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  std_msgs
  message_generation
  sensor_msgs
)

add_message_files(
   FILES
   msg1.msg
)

generate_messages(
  DEPENDENCIES
  std_msgs
  sensor_msgs
)

catkin_package(
  CATKIN_DEPENDS roscpp rospy std_msgs message_runtim
)

include_directories(
  ${catkin_INCLUDE_DIRS}
)

install(PROGRAMS
  scripts/pubMsg
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)

