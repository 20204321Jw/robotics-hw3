#!/usr/bin/env python
import rospy
from common_msgs.msg import cost_msg

def callback(msg):
    print "subscribe:", msg.int_data, msg.vel.linear.x, msg.vel.linear.y, msg.vel.linear.z, msg.vel.angular.x, msg.vel.angular.y, msg.vel.angular.z

rospy.init_node('cust_subscriber')
sub = rospy.Subscriber('cust_msg', cost_msg, callback)
rospy.spin()
    