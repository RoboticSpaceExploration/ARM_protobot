#!/usr/bin/python3
# license removed for brevity
import rospy
from std_msgs.msg import Float64

def talker():
    pub = rospy.Publisher('/arm/joint5_position_controller/command', Float64, queue_size=10)
    rospy.init_node('arm_talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        #hello_str = "hello world %s" % rospy.get_time()
        position = 2.0
        rospy.loginfo(position)
        pub.publish(position)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass

