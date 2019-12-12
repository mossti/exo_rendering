#!/usr/bin/env python

import roslib
import rospy
from std_msgs.msg import Int32MultiArray, Int64MultiArray
from geometry_msgs.msg import Twist
from RPi import GPIO
from time import sleep
import numpy as np
import math

def spool_callback(data):
	a = 0
	return

def motor_callback(data):
	a = 1
	return

def keyboard_callback(data):
	global a
	global b
	global spool_val_count
	global motor_val_count
	global spool_val_eq
	global motor_val_eq
	GPIO.setmode(GPIO.BCM)
	
	motor_vel = 20
	
	if data.angular.z < 0:
		GPIO.output(17,1)
		GPIO.output(22,0)
		GPIO.output(14,0)
		GPIO.output(15,1)
		a.ChangeDutyCycle(motor_vel)
		b.ChangeDutyCycle(motor_vel)
	
	if data.angular.z > 0:
		GPIO.output(17,0)
		GPIO.output(22,1)
		GPIO.output(14,1)
		GPIO.output(15,0)
		a.ChangeDutyCycle(motor_vel)
		b.ChangeDutyCycle(motor_vel)
	
	if data.angular.z == 0:
		GPIO.output(17,0)
		GPIO.output(22,0)
		GPIO.output(14,0)
		GPIO.output(15,0)
		a.ChangeDutyCycle(0)
		b.ChangeDutyCycle(0)
		
	rospy.loginfo(rospy.get_caller_id() + "I heard: " + str(data))
	return

def motor_init():
	global a
	global b
	global spool_val_count
	global motor_val_count
	global spool_val_eq
	global motor_val_eq
	
	spool_val_count = 0
	motor_val_count = 0
	
	GPIO.setmode(GPIO.BCM)
	GPIO.setup((17,27,22,14,15,24), GPIO.OUT)
	a = GPIO.PWM(27, 60)
	b = GPIO.PWM(24, 60)
	a.start(0)
	b.start(0)
	
	return

def motor_publisher():
	global a
	global b
	global spool_val_count
	global motor_val_count
	global spool_val_eq
	global motor_val_eq
	
	#GPIO.cleanup()
	
	rospy.init_node('motor_driver',anonymous=True)
	rospy.Subscriber("spool_encoder",Int64MultiArray,spool_callback)
	rospy.Subscriber("motor_encoder",Int32MultiArray,motor_callback)
	rospy.Subscriber("key_vel",Twist,keyboard_callback)
	
	rospy.spin()
	
	return

if __name__ == '__main__':
	try:
		GPIO.cleanup()
		GPIO.setmode(GPIO.BCM)
		motor_init()
		motor_publisher()
	except rospy.ROSInterruptException:
		GPIO.cleanup()
		pass
