#!/usr/bin/env python3
import rospy
from std_msgs.msg import Float64

def callback1(data):
    rospy.loginfo(rospy.get_caller_id() + " Joint1 moved %s radians", data.data)
    
def callback2(data):
    rospy.loginfo(rospy.get_caller_id() + " Joint2 moved %s radians", data.data)

def callback3(data):
    rospy.loginfo(rospy.get_caller_id() + " Joint3 moved %s radians", data.data)

def callback4(data):
    rospy.loginfo(rospy.get_caller_id() + " Joint4 moved %s radians", data.data)

def callback5(data):
    rospy.loginfo(rospy.get_caller_id() + " Joint5 moved %s radians", data.data)

def callback6(data):
    rospy.loginfo(rospy.get_caller_id() + " Joint6 moved %s radians", data.data)

def callback7(data):
    rospy.loginfo(rospy.get_caller_id() + " Joint7 moved %s radians", data.data)

def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('arm_control_subscriber_node', anonymous=True)

    rospy.Subscriber("/arm/joint1_position_controller/command", Float64, callback1)
    rospy.Subscriber("/arm/joint2_position_controller/command", Float64, callback2)
    rospy.Subscriber("/arm/joint3_position_controller/command", Float64, callback3)
    rospy.Subscriber("/arm/joint4_position_controller/command", Float64, callback4)
    rospy.Subscriber("/arm/joint5_position_controller/command", Float64, callback5)
    rospy.Subscriber("/arm/joint6_position_controller/command", Float64, callback6)
    rospy.Subscriber("/arm/joint7_position_controller/command", Float64, callback7)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
