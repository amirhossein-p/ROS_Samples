#!/usr/bin/env python
import rospy
from pack04.msg import msg1

def callbackMsg(data):
    # rospy.loginfo('Data is: %f', data.part_number)
    rospy.loginfo('Data is: %f', data.sensor_data.max_range)

def listenerMsg():
    rospy.init_node('listenerMsg', anonymous=True)
    rospy.Subscriber("chatterMsg", msg1, callbackMsg)
    rospy.spin()

if __name__ == '__main__':
    listenerMsg()
