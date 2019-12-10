#!/usr/bin/env python

import roslib
import rospy
from std_msgs.msg import Int32MultiArray, Int64MultiArray
from geometry_msgs.msg import Twist
from RPi import GPIO
from time import sleep
import numpy as np
import math

#a = 0
#b = 0
#spool_val_count = 0
#motor_val_count = 0

	#print "*       Modified SunFounder TB6612         *"
	#print "*                                          *"
	#print "*         Connect PWMA to BCM27            *"
	#print "*         Connect Ain1 to BCM17            *"
	#print "*         Connect Ain2 to BCM22            *"
	#print "*         Connect PWMB to BCM24            *"
	#print "*         Connect Bin1 to BCM14            *"
	#print "*         Connect Bin2 to BCM15            *"

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

def spool_callback(data):
	global a
	global b
	global spool_val_count
	global motor_val_count
	global spool_val_eq
	global motor_val_eq
	global spool_val_init_a
	global spool_val_init_b
	GPIO.setmode(GPIO.BCM)
	
	if spool_val_count == 0:
		spool_val_eq = data.data
		spool_val_init_a = (float(data.data[0])/4095)*360
		spool_val_init_b = (float(data.data[1])/4095)*360
	
	spool_val_a_mid = ((float(data.data[0] - spool_val_eq[0])/4095)*360)
	spool_val_b_mid = ((float(data.data[1] - spool_val_eq[1])/4095)*360)
	
	if spool_val_a_mid >= 0:
		spool_val_a = 0 + np.abs((float(data.data[0] - spool_val_eq[0])/4095)*360)
	if spool_val_a_mid < 0:
		spool_val_a = 360 - np.abs((float(data.data[0] - spool_val_eq[0])/4095)*360)
		
	
	if spool_val_b_mid >= 0:
		spool_val_b = 0 + np.abs((float(data.data[1] - spool_val_eq[1])/4095)*360)
	if spool_val_b_mid < 0:
		spool_val_b = 360 - np.abs((float(data.data[1] - spool_val_eq[1])/4095)*360)
	
	rospy.loginfo(rospy.get_caller_id() + " | spool_val_a: " + str(int(spool_val_a)) + " | spool_val_b: " + str(int(spool_val_b)))
	#rospy.loginfo(rospy.get_caller_id() + "spool_val_b: " + str(spool_val_b))
	
	if np.abs(spool_val_a - (360-spool_val_a)) >= 100:
		GPIO.output(17,1)
		GPIO.output(22,0)
		#GPIO.output(14,0)
		#GPIO.output(15,1)
		a.ChangeDutyCycle(15)
		
		
	if np.abs(spool_val_b - (360-spool_val_b)) >= 100:	
		#GPIO.output(17,0)
		#GPIO.output(22,1)
		GPIO.output(14,1)
		GPIO.output(15,0)
		b.ChangeDutyCycle(15)
		
	
	if np.abs(spool_val_a-spool_val_init_a) < 100:
		a.ChangeDutyCycle(0)
	
	if np.abs(spool_val_b-spool_val_init_b) < 100:
		b.ChangeDutyCycle(0)	
	
	
	spool_val_count += 1
	return

def motor_callback(data):
	global a
	global b
	global spool_val_count
	global motor_val_count
	global spool_val_eq
	global motor_val_eq
	GPIO.setmode(GPIO.BCM)
	
	
	if motor_val_count == 0:
		motor_val_eq = data.data
		
	motor_val_a = (float(data.data[0] - motor_val_eq[0])/250)*360
	motor_val_b = (float(data.data[1] - motor_val_eq[1])/250)*360
	
	#rospy.loginfo(rospy.get_caller_id() + "motor_val_a: " + str(motor_val_a))
	#rospy.loginfo(rospy.get_caller_id() + "motor_val_b: " + str(motor_val_b))
	
	#if motor_val_a >= (6*250)/4:
	#	GPIO.output(14,1)
	#	GPIO.output(15,0)
	#	a.ChangeDutyCycle(20)
		
	
	#if motor_val_b <= (6*250)/4:
	#	GPIO.output(14,0)
	#	GPIO.output(15,1)
	#	b.ChangeDutyCycle(20)
	
	#if np.abs(motor_val_a) < (6*250)/4:
	#	a.ChangeDutyCycle(0)
	
	#if np.abs(motor_val_b) < (6*250)/4:
	#	b.ChangeDutyCycle(0)	
	
	#a.ChangeDutyCycle(0)
	
	motor_val_count +=1
	return

def keyboard_callback(data):
	global a
	global b
	global spool_val_count
	global motor_val_count
	global spool_val_eq
	global motor_val_eq
	GPIO.setmode(GPIO.BCM)
	
	rospy.loginfo(rospy.get_caller_id() + "I heard: " + str(data))
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
	#rospy.Subscriber("key_vel",Twist,keyboard_callback)
	
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
