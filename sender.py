#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import rospy
from std_msgs.msg import Int16   # <-- Changed from Int32 to Int16

# Initialize node (name: sender_node)
rospy.init_node("sender_node", anonymous=False)

# Publisher to topic /box with message type Int16
pub = rospy.Publisher("/box", Int16, queue_size=10)

# Publish rate: every 3 seconds → 0.333 Hz
rate = rospy.Rate(0.333)

# Counter starts from 0
counter = 0
rospy.loginfo("[sender_node] Started, publishing Int16 to /box every 3s")

# Main loop
while not rospy.is_shutdown():
    msg = Int16()
    msg.data = counter

    pub.publish(msg)
    rospy.loginfo("[sender_node] Published: %d", counter)

    counter += 1
    rate.sleep()
