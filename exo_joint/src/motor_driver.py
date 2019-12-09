#!/usr/bin/env python

import roslib
import rospy
from std_msgs.msg import Int32MultiArray, Int64MultiArray
from RPi import GPIO
from time import sleep
import numpy as np
import math

	#print "*       Modified SunFounder TB6612         *"
	#print "*                                          *"
	#print "*         Connect PWMA to BCM27            *"
	#print "*         Connect Ain1 to BCM17            *"
	#print "*         Connect Ain2 to BCM22            *"
	#print "*         Connect PWMB to BCM24            *"
	#print "*         Connect Bin1 to BCM14            *"
	#print "*         Connect Bin2 to BCM15            *"

def spool_callback(data):
	rospy.loginfo(rospy.get_caller_id() + "I heard: " + str(data.data))
	return

def motor_callback(data):
	rospy.loginfo(rospy.get_caller_id() + "I heard: " + str(data.data))
	return

def motor_publisher():
	GPIO.cleanup()
	rospy.init_node('motor_driver',anonymous=True)
	rospy.Subscriber("spool_encoder",Int64MultiArray,spool_callback)
	rospy.Subscriber("motor_encoder",Int32MultiArray,motor_callback)
	#GPIO.setmode(GPIO.BCM)
	#GPIO.setup((17,27,22,14,15,24), GPIO.OUT)
	#a = GPIO.PWM(27, 60)
	#b = GPIO.PWM(24,60)

	#a.start(0)
	#b.start(0)
	
	rospy.spin()
	
	return

if __name__ == '__main__':
	try:
		GPIO.cleanup()
		motor_publisher()
	except rospy.ROSInterruptException:
		GPIO.cleanup()
		pass
