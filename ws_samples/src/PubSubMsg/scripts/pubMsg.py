#!/usr/bin/env python
import rospy
from PubSubMsg.msg import msg1

def talkerMsg():
    pub1 = rospy.Publisher('chatterMsg', msg1, queue_size=10)
    rospy.init_node('talkerMsg', anonymous=True)
    rate = rospy.Rate(1) # 10hz
    msg_info = msg1()
    msg_info.sensor_data.header.stamp = rospy.Time.now()
    msg_info.sensor_data.max_range = 2.00
    msg_info.maker_name = 'SICK'
    while not rospy.is_shutdown():
        pub1.publish(msg_info)
        rate.sleep()

if __name__ == '__main__':
    try:
        talkerMsg()
    except rospy.ROSInterruptException:
        pass
