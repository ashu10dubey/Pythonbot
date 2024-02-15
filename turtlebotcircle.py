#!/usr/bin/env python 3
import rospy
from geometry_msgs.msg import Twist

if __name__ == '__main__':
    rospy.init_node('check')
    rospy.loginfo("started")
    pub = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size=10)
    rate = rospy.Rate(5)

    r = 2  # radius in cm
    omega = 2  # angular velocity in rad/s
    v = r * omega  # linear velocity in cm/s

    while not rospy.is_shutdown():
        msg = Twist()
        msg.linear.x = v
        msg.angular.z = omega
        pub.publish(msg)
        rate.sleep()