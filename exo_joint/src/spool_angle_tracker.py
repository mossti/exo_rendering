#!/usr/bin/env python

import roslib
import rospy
from std_msgs.msg import Int64MultiArray
from RPi import GPIO
from time import sleep
import numpy as np
import math

# Three-wire SSI for AEAT-601012
# (#1) CS = 0, DO = 1, CLK = 3
# (#2) CS = 5, DO = 6, CLK = 7

def init_spool_encoders():
	GPIO.output(0,1)
	GPIO.output(3,1)
	GPIO.output(5,1)
	GPIO.output(7,1)
	
	return

def start_read():
	GPIO.output(0,0)
	GPIO.output(5,0)
	a = GPIO.input(1)
	b = GPIO.input(6)
	
	sleep(0.0000001)
	a = GPIO.input(1)
	b = GPIO.input(6)
	
	sleep(0.0000004)
	a = GPIO.input(1)
	b = GPIO.input(6)
	
	GPIO.output(3,0)
	GPIO.output(7,0)
	a = GPIO.input(1)
	b = GPIO.input(6)
	
	return


def spool_angle_publisher():
	global entry_array
	pub = rospy.Publisher('spool_encoder', Int64MultiArray, queue_size=10)
	rospy.init_node('publisher', anonymous=True)
	rate = rospy.Rate(1000)
	
	entry_array = Int64MultiArray()
	entry_array.data = []
	
	GPIO.setmode(GPIO.BCM)
	GPIO.setup((0,3), GPIO.OUT)
	GPIO.setup((5,7), GPIO.OUT)
	GPIO.setup(1,GPIO.IN)
	GPIO.setup(6,GPIO.IN)
	
	init_spool_encoders()
	
	sleep(0.2)
	
	while not rospy.is_shutdown():

		entry = np.array([0])
		
		init_spool_encoders()
		
		sleep(0.0000005)
		
		start_read()
		
		sleep(5/1000000.0)
		
		for i in range(0,12):
			
			GPIO.output(3,1)
			GPIO.output(7,1)
			
			sleep(0.000000375)
			
			a = GPIO.input(1)
			b = GPIO.input(6)
			
			sleep(0.000000125)
			
			GPIO.output(3,0)
			GPIO.output(7,0)
			
			sleep(0.0000005)
			
			if i == 0:
				#entry[0] = a
				entry_a = str(a)
				entry_b = str(b)
			else:
				#entry = np.append(entry, a)
				entry_a = entry_a + str(a)
				entry_b = entry_b + str(b)
		
		entry_a = int(entry_a,2)
		entry_b = int(entry_b,2)
		rospy.loginfo(rospy.get_caller_id() + "spool_val_a: " + str(entry_a))
		rospy.loginfo(rospy.get_caller_id() + "spool_val_b: " + str(entry_b))
		entry_array.data = [entry_a, entry_b]
		pub.publish(entry_array)
		#rate.sleep()
	
	GPIO.cleanup()
	
	return

if __name__ == '__main__':
	try:
		GPIO.cleanup()
		spool_angle_publisher()
	except rospy.ROSInterruptException:
		GPIO.cleanup()
		pass
