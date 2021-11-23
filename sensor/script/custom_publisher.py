#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from common_msgs.msg import cost_msg

rospy.init_node('cust_publisher')
pub = rospy.Publisher('cust_msg', cost_msg, queue_size=1)
msg = cost_msg()
rate = rospy.Rate(1)
while not rospy.is_shutdown():
    msg.int_data.data = 3
    msg.vel.linear.x = 1
    msg.vel.linear.y = 2
    msg.vel.linear.z = 3
    msg.vel.angular.x = 1
    msg.vel.angular.y = 2
    msg.vel.angular.z = 3 
    pub.publish(msg)
    print "publish:", msg.int_data, msg.vel.linear.x, msg.vel.linear.y, msg.vel.linear.z, msg.vel.angular.x, msg.vel.angular.y, msg.vel.angular.z
    rate.sleep()
