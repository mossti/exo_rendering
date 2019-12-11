#!/usr/bin/env python

import roslib
import rospy
from std_msgs.msg import Int32MultiArray
from RPi import GPIO
from time import sleep
import numpy as np
import math

def init_motor_encoders():
	global clk1
	global clk2
	global dt1
	global dt2
	global counter1
	global counter2
	global clkLastState1
	global clkLastState2
	
	clk2 = 19 #A1
	clk1 = 16 #B1
	dt2 = 26 #A2
	dt1 = 20 #B2

	GPIO.setmode(GPIO.BCM)
	GPIO.setup(clk1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
	GPIO.setup(clk2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
	GPIO.setup(dt1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
	GPIO.setup(dt2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

	counter1 = 0
	counter2 = 0
	clkLastState1 = GPIO.input(clk1)
	clkLastState2 = GPIO.input(clk2)
	
	return clk1, clk2, dt1, dt2, counter1, counter2, clkLastState1, clkLastState2


def motor_angle_publisher():
	global counter_array
	pub = rospy.Publisher('motor_encoder', Int32MultiArray, queue_size=10)
	rospy.init_node('publisher', anonymous=True)
	rate = rospy.Rate(1000)
	
	counter_array = Int32MultiArray()
	counter_array.data = []
	
	clk1, clk2, dt1, dt2, counter1, counter2, clkLastState1, clkLastState2 = init_motor_encoders()
	
	while not rospy.is_shutdown():
		
		clkState1 = GPIO.input(clk1)
		clkState2 = GPIO.input(clk2)
		dtState1 = GPIO.input(dt1)
		dtState2 = GPIO.input(dt2)
		if clkState1 != clkLastState1:
				if dtState1 != clkState1:
						counter1 += 1
				else:
						counter1 -= 1
				print counter1
				
		if clkState2 != clkLastState2:
				if dtState2 != clkState2:
						counter2 += 1
				else:
						counter2 -= 1
				print counter2
				
		clkLastState1 = clkState1
		clkLastState2 = clkState2
		
		counter_array.data = [counter1, counter2]
		
		pub.publish(counter_array)
		
		sleep(0.01)
    
		#rate.sleep()
	
	GPIO.cleanup()
	
	return

if __name__ == '__main__':
	try:
		GPIO.cleanup()
		motor_angle_publisher()
	except rospy.ROSInterruptException:
		GPIO.cleanup()
		pass
