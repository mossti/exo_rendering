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

def pid_control(delta_theta, int_error, delta_error):
	kp = 1
	ki = 5
	kd = 5
	vel = kp*delta_theta + ki*int_error + kd*delta_error
	if vel < 5:
		vel = 5
	if vel >= 30:
		vel = 30
	return vel

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
	global spool_val_a
	global spool_val_b
	global spool_val_init_a
	global spool_val_init_b
	global motor_val_init_a
	global motor_val_init_b
	global spool_val_last_a
	global spool_val_last_b
	global motor_val_last_a
	global motor_val_last_b
	
	global spool_val_high_a
	global spool_val_low_a
	global motor_val_high_a
	global motor_val_low_a
	global spool_val_high_b
	global spool_val_low_b
	global motor_val_high_b
	global motor_val_low_b
	
	global max_deflection
	GPIO.setmode(GPIO.BCM)
	
	if spool_val_count == 0:
		spool_val_eq = data.data
		spool_val_init_a = (float(spool_val_eq[0])/4095)*360 - (float(spool_val_eq[0])/4095)*360
		spool_val_init_b = (float(spool_val_eq[1])/4095)*360 - (float(spool_val_eq[1])/4095)*360
	
	
	
	spool_val_a_mid = ((float(data.data[0] - spool_val_eq[0])/4095)*360)
	spool_val_b_mid = ((float(data.data[1] - spool_val_eq[1])/4095)*360)
	
	if spool_val_a_mid >= 0:
		#spool_val_a = 0 + np.abs((float(data.data[0] - spool_val_eq[0])/4095)*360)
		spool_val_a = 0 + np.abs((float(data.data[0])/4095)*360 - (float(spool_val_eq[0])/4095)*360)
	if spool_val_a_mid < 0:
		#spool_val_a = 360 - np.abs((float(data.data[0] - spool_val_eq[0])/4095)*360)
		spool_val_a = 360 - np.abs((float(data.data[0])/4095)*360 - (float(spool_val_eq[0])/4095)*360)
		
	
	if spool_val_b_mid >= 0:
		spool_val_b = 0 + np.abs((float(data.data[1])/4095)*360 - (float(spool_val_eq[1])/4095)*360)
	if spool_val_b_mid < 0:
		spool_val_b = 360 - np.abs((float(data.data[1])/4095)*360 - (float(spool_val_eq[1])/4095)*360)
	
	#rospy.loginfo(rospy.get_caller_id() + " | spool_val_a: " + str(int(spool_val_init_a)) + "/" + str(int(spool_val_a)) + " | spool_val_b: " + str(int(spool_val_init_b)) + "/" + str(int(spool_val_b)))
	#rospy.loginfo(rospy.get_caller_id() + "spool_val_b: " + str(spool_val_b))
	#rospy.loginfo(rospy.get_caller_id() + " | " + str(int(((360-spool_val_init_a) - (360-spool_val_a)))) + " | " + str(int(((360-spool_val_init_b) - (360-spool_val_b)))))
	
	#if ((360-spool_val_init_a) - (360-spool_val_a)) >= 100:
	#if (spool_val_a >= (spool_val_init_a + 180)):
	#	if np.abs(spool_val_init_a - (360-spool_val_a)) >= 100:
	#		if 360-spool_val_a > (spool_val_init_a):
	#			GPIO.output(17,1)
	#			GPIO.output(22,0)
	#			a.ChangeDutyCycle(15)
	#		if 360-spool_val_a < (spool_val_init_a):
	#			GPIO.output(17,0)
	#			GPIO.output(22,1)
	#			a.ChangeDutyCycle(15)
				
	#if (spool_val_a < (spool_val_init_a + 180)):
	#	if np.abs(spool_val_init_a - (360-spool_val_a)) >= 100:
	#		if 360-spool_val_a > spool_val_init_a:
	#			GPIO.output(17,0)
	#			GPIO.output(22,1)
	#			a.ChangeDutyCycle(15)
	#		if 360-spool_val_a < spool_val_init_a:
	#			GPIO.output(17,1)
	#			GPIO.output(22,0)
	#			a.ChangeDutyCycle(15)
				
	#if (spool_val_b >= (spool_val_init_b + 180)):			
	#	if np.abs(spool_val_init_b - (360-spool_val_b)) >= 100:
	#		if 360-spool_val_a > spool_val_init_b:
	#			GPIO.output(14,0)
	#			GPIO.output(15,1)
	#			b.ChangeDutyCycle(15)
	#		if 360-spool_val_a < spool_val_init_b:
	#			GPIO.output(14,1)
	#			GPIO.output(15,0)
	#			b.ChangeDutyCycle(15)
	
	
	#if (spool_val_b < (spool_val_init_b + 180)):
	#	if np.abs(spool_val_init_b - (360-spool_val_b)) >= 100:
	#		if 360-spool_val_a > spool_val_init_b:
	#			GPIO.output(14,1)
	#			GPIO.output(15,0)
	#			b.ChangeDutyCycle(15)
	#		if 360-spool_val_a < spool_val_init_b:
	#			GPIO.output(14,0)
	#			GPIO.output(15,1)
	#			b.ChangeDutyCycle(15)
			
	
	#if np.abs(spool_val_a-spool_val_init_a) < 100:
	#	a.ChangeDutyCycle(0)
	
	#if np.abs(spool_val_b-spool_val_init_b) < 100:
	#	b.ChangeDutyCycle(0)	
	
	
	spool_val_count += 1
	spool_val_last_a = spool_val_a
	spool_val_last_b = spool_val_b
	return

def motor_callback(data):
	global a
	global b
	global spool_val_count
	global motor_val_count
	global spool_val_eq
	global motor_val_eq
	global spool_val_a
	global spool_val_b
	global spool_val_init_a
	global spool_val_init_b
	global motor_val_init_a
	global motor_val_init_b
	global spool_val_last_a
	global spool_val_last_b
	global motor_val_last_a
	global motor_val_last_b
	global spool_val_a_track
	global spool_val_b_track
	
	global spool_val_high_a
	global spool_val_low_a
	global motor_val_high_a
	global motor_val_low_a
	global spool_val_high_b
	global spool_val_low_b
	global motor_val_high_b
	global motor_val_low_b
	
	global dist_a
	global dist_b
	global dist_a_last
	global dist_b_last
	
	global delta_a
	global delta_b
	global int_delta_a
	global int_delta_b
	
	global flag_a
	global flag_b
	
	global turn_tracker_a
	global turn_tracker_b
	
	global test
	
	global max_deflection
	GPIO.setmode(GPIO.BCM)
		
	if motor_val_count == 0:
		max_deflection = 20
		motor_val_eq = data.data
		spool_val_a = 0
		spool_val_b = 0
		spool_val_last_a = 0
		spool_val_last_b = 0
		motor_val_last_a = 0
		motor_val_last_b = 0
		spool_val_a_track = 0
		spool_val_b_track = 0
		motor_val_a_track = 0
		motor_val_b_track = 0
		
		spool_val_high_a = 0
		spool_val_low_a = 0
		motor_val_high_a = 0
		motor_val_low_a = 0
		spool_val_high_b = 0
		spool_val_low_b = 0
		motor_val_high_b = 0
		motor_val_low_b = 0
		
		dist_a = 0
		dist_b = 0
		dist_a_last = dist_a
		dist_b_last = dist_b
		
		delta_a = 0
		delta_b = 0
		int_delta_a = 0
		int_delta_b = 0
		
		flag_a = '...'
		flag_b = '...'
		turn_tracker_a = 0
		turn_tracker_b = 0
	
	test = '2'
	
	motor_val_a = ((float(data.data[0] - motor_val_eq[0])/250)*360)%360
	motor_val_b = ((float(data.data[1] - motor_val_eq[1])/250)*360)%360
	
	#rospy.loginfo(str(dist_a))
	#rospy.loginfo(str(dist_b))
	#rospy.loginfo(str(dist_a_last))
	#rospy.loginfo(str(dist_b_last))
	#rospy.loginfo(str(delta_a))
	#rospy.loginfo(str(delta_b))
	#rospy.loginfo(str(int_delta_a))
	#rospy.loginfo(str(int_delta_b))
	
	#rospy.loginfo(rospy.get_caller_id() + " | " + "motor_val_a: " + str(int(motor_val_eq[0])) + "/" + str(int(motor_val_a)) + " | " + "motor_val_b: " + str(int(motor_val_eq[1])) + "/" + str(int(motor_val_b)))
	#rospy.loginfo(rospy.get_caller_id() + "motor_val_b: " + str(motor_val_b))
	
	#rospy.loginfo(str(int(motor_val_a)) + "/" + str(int(spool_val_a)) + " | " + str(int(motor_val_b)) + "/" + str(int(spool_val_b)))
	#rospy.loginfo(str(int(spool_val_a%360 - motor_val_a%360)) + " | " + str(int(spool_val_b%360 - motor_val_b%360)))
	#rospy.loginfo(str(int(spool_val_a - (360-motor_val_a))) + " | " + str(int(spool_val_b - (360-motor_val_b))))
	#rospy.loginfo(str(int(np.abs(spool_val_a - (360-motor_val_a)))) + " | " + str(int(np.abs(spool_val_b - (360-motor_val_b)))))
	
	#rospy.loginfo(str(int(motor_val_a-motor_val_last_a)) + " | " + str(int(spool_val_a-spool_val_last_a)))
	
	#rospy.loginfo(str(int(spool_val_a)) + " | " + str(int(spool_val_a_track)) + "    ...    " + str(int(np.abs(motor_val_a - spool_val_a_track))) + "/" + str(int(max_deflection)) + " || " + str(int(spool_val_b)) + " | " + str(int(spool_val_b_track)) + "    ...    " + str(int(np.abs(motor_val_b - spool_val_b_track))) + "/" + str(int(max_deflection)))
	
	
	### PID VELOCITY CONTROL TERMS
	delta_a = dist_a_last - dist_a
	delta_b = dist_b_last - dist_b
	
	int_delta_a += delta_a
	int_delta_b += delta_b
	
	motor_v_a = pid_control(dist_a, int_delta_a, delta_a)
	motor_v_b = pid_control(dist_b, int_delta_b, delta_b)
	
	#motor_v_a = 15
	#motor_v_b = 15
	
	if (motor_val_last_a > 0 and motor_val_last_a < 180) and (motor_val_a > 180):
		turn_tracker_a -= 1
	
	if (motor_val_last_a > 180) and (motor_val_a > 0 and motor_val_a < 180):
		turn_tracker_a +=1
	
	if (motor_val_last_b > 0 and motor_val_last_b < 180) and (motor_val_b > 180):
		turn_tracker_b -= 1
	
	if (motor_val_last_b > 180) and (motor_val_b > 0 and motor_val_b < 180):
		turn_tracker_b +=1
	
	spool_val_low_a = 0 + spool_val_a
	spool_val_high_a = 360 - spool_val_a
	motor_val_low_a = 0 + motor_val_a
	motor_val_high_a = 360 - motor_val_a
	
	spool_val_low_b = 0 + spool_val_b
	spool_val_high_b = 360 - spool_val_b
	motor_val_low_b = 0 + motor_val_b
	motor_val_high_b = 360 - motor_val_b
	
	# MOTOR CORRECTS ELASTIC DEVIATION CASE; TEST = '1'
	if test == '1':
	
		if spool_val_a > motor_val_a:
			dist_low_a = spool_val_high_a + motor_val_low_a
			dist_high_a = spool_val_a - motor_val_a
			if dist_low_a < dist_high_a:
				dist_a = dist_low_a
				if dist_a > max_deflection:
					#rospy.loginfo("SVA > MVA ; DIST_LOW < DIST_HIGH ; DIST A > MAX DEFLECTION")
					GPIO.output(17,0)
					GPIO.output(22,1)
					a.ChangeDutyCycle(motor_v_a)
					flag_a = "-->"
			if dist_high_a < dist_low_a:
				dist_a = dist_high_a
				if dist_a > max_deflection:
					#rospy.loginfo("SVA > MVA ; DIST_LOW > DIST_HIGH ; DIST A > MAX DEFLECTION")
					GPIO.output(17,1)
					GPIO.output(22,0)
					a.ChangeDutyCycle(motor_v_a)
					flag_a = "<--"
				
		if spool_val_a < motor_val_a:
			dist_low_a = spool_val_low_a + motor_val_high_a
			dist_high_a = motor_val_a - spool_val_a
			if dist_low_a < dist_high_a:
				dist_a = dist_low_a
				if dist_a > max_deflection:
					#rospy.loginfo("SVA < MVA ; DIST_LOW < DIST_HIGH ; DIST A > MAX DEFLECTION")
					GPIO.output(17,0)
					GPIO.output(22,1)
					flag_a = "-->"
					a.ChangeDutyCycle(motor_v_a)
			if dist_high_a < dist_low_a:
				dist_a = dist_high_a
				if dist_a > max_deflection:
					#rospy.loginfo("SVA < MVA ; DIST_LOW > DIST_HIGH ; DIST A > MAX DEFLECTION")
					GPIO.output(17,1)
					GPIO.output(22,0)
					a.ChangeDutyCycle(motor_v_a)
					flag_a = "<--"
					
		if spool_val_b > motor_val_b:
			dist_low_b = spool_val_high_b + motor_val_low_b
			dist_high_b = spool_val_b - motor_val_b
			if dist_low_b < dist_high_b:
				dist_b = dist_low_b
				if dist_b > max_deflection:
					#rospy.loginfo("SVB > MVB ; DIST_LOW < DIST_HIGH ; DIST B > MAX DEFLECTION")
					GPIO.output(14,1)
					GPIO.output(15,0)
					b.ChangeDutyCycle(motor_v_b)
					flag_b = "-->"
			if dist_high_b < dist_low_b:
				dist_b = dist_high_b
				if dist_b > max_deflection:
					#rospy.loginfo("SVB > MVB ; DIST_LOW > DIST_HIGH ; DIST B > MAX DEFLECTION")
					GPIO.output(14,0)
					GPIO.output(15,1)
					b.ChangeDutyCycle(motor_v_b)
					flag_b = "<--"
					
		if spool_val_b < motor_val_b:
			dist_low_b = spool_val_low_b + motor_val_high_b
			dist_high_b = motor_val_b - spool_val_b
			if dist_low_b < dist_high_b:
				dist_b = dist_low_b
				if dist_b > max_deflection:
					#rospy.loginfo("SVB < MVB ; DIST_LOW < DIST_HIGH ; DIST B > MAX DEFLECTION")
					GPIO.output(14,1)
					GPIO.output(15,0)
					b.ChangeDutyCycle(motor_v_b)
					flag_b = "-->"
			if dist_high_b < dist_low_b:
				dist_b = dist_high_b
				if dist_b > max_deflection:
					#rospy.loginfo("SVB < MVB ; DIST_LOW > DIST_HIGH ; DIST B > MAX DEFLECTION")
					GPIO.output(14,0)
					GPIO.output(15,1)
					b.ChangeDutyCycle(motor_v_b)
					flag_b = "<--"
	
		if dist_a < max_deflection-5:
			GPIO.output(17,0)
			GPIO.output(22,0)
			a.ChangeDutyCycle(0)
			flag_a = "..."
		if dist_b < max_deflection-5:
			GPIO.output(14,0)
			GPIO.output(15,0)
			b.ChangeDutyCycle(0)
			flag_b = "..."
	
	# MOTOR FOLLOWS ELASTIC DEVIATION CASE; TEST = '2'
	if test == '2':
	
		if spool_val_a > motor_val_a:
			dist_low_a = spool_val_high_a + motor_val_low_a
			dist_high_a = spool_val_a - motor_val_a
			if dist_low_a <=  dist_high_a:
				dist_a = dist_low_a
				if dist_a > max_deflection:
					#rospy.loginfo("SVA > MVA ; DIST_LOW < DIST_HIGH ; DIST A > MAX DEFLECTION")
					GPIO.output(17,0)
					GPIO.output(22,1)
					a.ChangeDutyCycle(motor_v_a)
					flag_a = "<-- (1)"
					
				
					
			if dist_high_a < dist_low_a:
				dist_a = dist_high_a
				if dist_a > max_deflection:
					#rospy.loginfo("SVA > MVA ; DIST_LOW > DIST_HIGH ; DIST A > MAX DEFLECTION")
					GPIO.output(17,1)
					GPIO.output(22,0)
					a.ChangeDutyCycle(motor_v_a)
					flag_a = "--> (2)"
					
				
			
					
				
		if spool_val_a < motor_val_a:
			dist_low_a = spool_val_low_a + motor_val_high_a
			dist_high_a = motor_val_a - spool_val_a
			if dist_low_a <= dist_high_a:
				dist_a = dist_low_a
				if dist_a > max_deflection:
					#rospy.loginfo("SVA < MVA ; DIST_LOW < DIST_HIGH ; DIST A > MAX DEFLECTION")
					GPIO.output(17,1)
					GPIO.output(22,0)
					flag_a = "--> (3)"
					a.ChangeDutyCycle(motor_v_a)
					pass
				pass
			pass
				
			if dist_high_a < dist_low_a:
				dist_a = dist_high_a
				if dist_a > max_deflection:
					#rospy.loginfo("SVA < MVA ; DIST_LOW > DIST_HIGH ; DIST A > MAX DEFLECTION")
					GPIO.output(17,0)
					GPIO.output(22,1)
					a.ChangeDutyCycle(motor_v_a)
					flag_a = "<-- (4)"
					pass
				pass
			pass
			
		if spool_val_b > motor_val_b:
			dist_low_b = spool_val_high_b + motor_val_low_b
			dist_high_b = spool_val_b - motor_val_b
			if dist_low_b <= dist_high_b:
				dist_b = dist_low_b
				if dist_b > max_deflection:
					#rospy.loginfo("SVB > MVB ; DIST_LOW < DIST_HIGH ; DIST B > MAX DEFLECTION")
					GPIO.output(14,0)
					GPIO.output(15,1)
					b.ChangeDutyCycle(motor_v_b)
					flag_b = "<-- (1)"
			if dist_high_b < dist_low_b:
				dist_b = dist_high_b
				if dist_b > max_deflection:
					#rospy.loginfo("SVB > MVB ; DIST_LOW > DIST_HIGH ; DIST B > MAX DEFLECTION")
					GPIO.output(14,1)
					GPIO.output(15,0)
					b.ChangeDutyCycle(motor_v_b)
					flag_b = "--> (2)"
					
		if spool_val_b < motor_val_b:
			dist_low_b = spool_val_low_b + motor_val_high_b
			dist_high_b = motor_val_b - spool_val_b
			if dist_low_b <= dist_high_b:
				dist_b = dist_low_b
				if dist_b > max_deflection:
					#rospy.loginfo("SVB < MVB ; DIST_LOW < DIST_HIGH ; DIST B > MAX DEFLECTION")
					GPIO.output(14,1)
					GPIO.output(15,0)
					b.ChangeDutyCycle(motor_v_b)
					flag_b = "--> (3)"
			if dist_high_b < dist_low_b:
				dist_b = dist_high_b
				if dist_b > max_deflection:
					#rospy.loginfo("SVB < MVB ; DIST_LOW > DIST_HIGH ; DIST B > MAX DEFLECTION")
					GPIO.output(14,0)
					GPIO.output(15,1)
					b.ChangeDutyCycle(motor_v_b)
					flag_b = "<-- (4)"
	
		if dist_a < 10:
			GPIO.output(17,0)
			GPIO.output(22,0)
			a.ChangeDutyCycle(0)
			flag_a = "..."
			
		if dist_b < 10:
			GPIO.output(14,0)
			GPIO.output(15,0)
			b.ChangeDutyCycle(0)
			flag_b = "..."
			
		
	rospy.loginfo("assembly a: " + str(int(spool_val_a)) + "/" + str(int(motor_val_a)) + " | " + str(int(dist_a)) + "/" + str(int(max_deflection)) + " : " + str(motor_v_a) + flag_a + " || " + "assembly b: " + str(int(spool_val_b)) + "/" + str(int(motor_val_b)) + " | " + str(int(dist_b)) + "/" + str(int(max_deflection)) + " : " + str(motor_v_b) + flag_b + " || " + str(turn_tracker_a) + " | " + str(turn_tracker_b))
	
	
	#rospy.loginfo(str(turn_tracker_a) + " | " + str(turn_tracker_b))
	#rospy.loginfo(str(int(motor_val_last_a)) + "/" + str(int(motor_val_a)) + " || " + str(int(motor_val_last_b)) + "/" + str(int(motor_val_b)))
	
	#if spool_val_a >= (motor_val_a + 180):
	#	spool_val_a_track = -(360 - spool_val_a)
	
	#if spool_val_a < (motor_val_a + 180):
	#	spool_val_a_track = spool_val_a
	
	#if spool_val_b >= (motor_val_b + 180):
	#	spool_val_b_track = -(360 - spool_val_b)
	
	#if spool_val_b < (motor_val_b + 180):
	#	spool_val_b_track = spool_val_b
	
	#if motor_val_a >= 180:
	#	motor_val_a_track = -(360 - motor_val_a)
	
	#if motor_val_a < 180:
	#	motor_val_a_track = motor_val_a
	
	#if motor_val_b >= 180:
	#	motor_val_b_track = -(360 - motor_val_b)
	
	#if motor_val_b < 180:
	#	motor_val_b_track = motor_val_b
	
	#if motor_val_a > 180:
	#	motor_val_a_track = np.abs(0 - spool_val_a)
	
	#if np.abs(motor_val_a - spool_val_a_track) >= max_deflection:
	#	if spool_val_a_track >= 0:
	#		GPIO.output(17,0)
	#		GPIO.output(22,1)
	#		a.ChangeDutyCycle(20)
	#	if spool_val_a_track < 0:
	#		GPIO.output(17,1)
	#		GPIO.output(22,0)
	#		a.ChangeDutyCycle(20)
	#else:
	#	a.ChangeDutyCycle(0)


	#if np.abs(motor_val_b - spool_val_b_track) >= max_deflection:
	#	if spool_val_a_track >= 0:
	#		GPIO.output(14,1)
	#		GPIO.output(15,0)
	#		b.ChangeDutyCycle(20)
	#	if spool_val_a_track < 0:
	#		GPIO.output(14,0)
	#		GPIO.output(15,1)
	#		b.ChangeDutyCycle(20)
	#else:
	#	b.ChangeDutyCycle(0)
		
	#if spool_val_a >= (motor_val_a + 180)%360:
		#if np.abs(spool_val_a - (360-motor_val_a)) >= max_deflection:
			#if 360-spool_val_a >= motor_val_a:
			#GPIO.output(17,1)
			#GPIO.output(22,0)
			#a.ChangeDutyCycle(15)
			#if 360-spool_val_a < motor_val_a:
			#	GPIO.output(17,0)
			#	GPIO.output(22,1)
			#	a.ChangeDutyCycle(15)
		#else:
		#	a.ChangeDutyCycle(0)

				
	#if spool_val_a < (motor_val_a + 180)%360:
		#if np.abs(spool_val_a - (360-motor_val_a)) >= max_deflection:
			#if 360-spool_val_a >= motor_val_a:
			#GPIO.output(17,0)
			#GPIO.output(22,1)
			#a.ChangeDutyCycle(15)
			#if 360-spool_val_a < motor_val_a:
			#	GPIO.output(17,1)
			#	GPIO.output(22,0)
			#	a.ChangeDutyCycle(15)
		#else:
			#a.ChangeDutyCycle(0)
	
	#if np.abs(spool_val_a%360 - motor_val_a%360) >= max_deflection:
	#	if (spool_val_a%360 - motor_val_a%360) < 0.0:
	#		GPIO.output(17,1)
	#		GPIO.output(22,0)
	#		a.ChangeDutyCycle(15)
	#	if (spool_val_a%360 - motor_val_a%360) > 0.0:
	#		GPIO.output(17,0)
	#		GPIO.output(22,1)
	#		a.ChangeDutyCycle(15)
	
	#if np.abs(spool_val_a%360 - motor_val_a%360) < max_deflection:
	#	a.ChangeDutyCycle(0)
	
	#if np.abs(spool_val_b%360 - motor_val_b%360) >= max_deflection:
	#	if (spool_val_b%360 - motor_val_b%360) < 0.0:
	#		GPIO.output(14,0)
	#		GPIO.output(15,1)
	#		b.ChangeDutyCycle(15)
	#	if (spool_val_b%360 - motor_val_b%360) > 0.0:
	#		GPIO.output(14,1)
	#		GPIO.output(15,0)
	#		b.ChangeDutyCycle(15)
	
	#if np.abs(spool_val_b%360 - motor_val_b%360) < max_deflection:
	#	b.ChangeDutyCycle(0)
		
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
	motor_val_last_a = motor_val_a
	motor_val_last_b = motor_val_b
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
