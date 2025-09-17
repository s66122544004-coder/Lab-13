#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import rospy
from std_msgs.msg import Int16

# Callback runs whenever a new message arrives on /box
def callback(msg):
    rospy.loginfo("[receiver_node] Received from /box: %d", msg.data)

# Initialize node with name receiver_node
rospy.init_node("receiver_node", anonymous=False)

# Subscribe to /box topic (message type: Int16)
rospy.Subscriber("/box", Int16, callback)

# Keep the node alive to keep receiving messages
rospy.spin()

