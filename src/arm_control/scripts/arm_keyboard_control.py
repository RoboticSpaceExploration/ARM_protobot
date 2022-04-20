#!/usr/bin/python3
# license removed for brevity
import rospy
from std_msgs.msg import Float64
import sys, select, os
if os.name == 'nt':
  import msvcrt
else:
  import tty, termios


#Check what key is being pressed. 
def getKey():
    if os.name == 'nt':
      return msvcrt.getch()

    tty.setraw(sys.stdin.fileno())
    rlist, _, _ = select.select([sys.stdin], [], [], 0.1)
    if rlist:
        key = sys.stdin.read(1)
    else:
        key = ''

    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
    return key

#Left Finger Joint1
def joint1():
    pub = rospy.Publisher('/arm/joint5_position_controller/command', Float64, queue_size=10)
    rospy.init_node('leftFinger', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        position = 0.5
        rospy.loginfo(position)
        pub.publish(position)
        rate.sleep()


#Right Finger Joint2 
def joint2():
    pub = rospy.Publisher('/arm/joint5_position_controller/command', Float64, queue_size=10)
    rospy.init_node('rightFinger', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        position = 0.5
        rospy.loginfo(position)
        pub.publish(position)
        rate.sleep()


#End Actuator Spin Joint3
def joint3():
    pub = rospy.Publisher('/arm/joint5_position_controller/command', Float64, queue_size=10)
    rospy.init_node('endSpin', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        position = 0.5
        rospy.loginfo(position)
        pub.publish(position)
        rate.sleep()

#End Actuator Up and Down Joint4
def joint4():
    pub = rospy.Publisher('/arm/joint4_position_controller/command', Float64, queue_size=10)
    rospy.init_node('endUD', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        position = 0.5
        rospy.loginfo(position)
        pub.publish(position)
        rate.sleep()

#Middle of Arm Up and Down Joint5
def joint5():
    pub = rospy.Publisher('/arm/joint5_position_controller/command', Float64, queue_size=10)
    rospy.init_node('midUD', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        position = 0.5
        rospy.loginfo(position)
        pub.publish(position)
        rate.sleep()


#Bottom of Arm Up and Down Joint6
def joint6():
    pub = rospy.Publisher('/arm/joint6_position_controller/command', Float64, queue_size=10)
    rospy.init_node('botUD', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        position = 0.5
        rospy.loginfo(position)
        pub.publish(position)
        rate.sleep()


#Bottom of Arm Spin Joint7
def joint7():
    pub = rospy.Publisher('/arm/joint7_position_controller/command', Float64, queue_size=10)
    rospy.init_node('botSpin', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        position = 0.5 
        rospy.loginfo(position)
        pub.publish(position)
        rate.sleep()



if __name__ == '__main__':
    if os.name != 'nt':
        settings = termios.tcgetattr(sys.stdin)

    try:
       while(1):
           key = getKey()
           if key == 'w' :
               joint3()
           elif key == 'x' : 
               joint4()
           elif key == 'd' : 
               joint5()
           elif key == 'a' : 
               joint6()
           elif key == 's' : 
               joint7()

#        joint1() #Left  Finger 
#        joint2() #Right Finger
#        joint3() #End Actuator Spin
#        joint4() #End Actuator Up and Down
#        joint5() #Middle Arm Up and Down
#        joint6() #Bottom Arm Up and Down
#        joint7() #Bottom Arm Spin

    except rospy.ROSInterruptException:
        pass


