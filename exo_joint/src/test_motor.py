#!/usr/bin/env python
import time
import RPi.GPIO as GPIO

def main():
	import time

	print "********************************************"
	print "*                                          *"
	print "*       Modified SunFounder TB6612         *"
	print "*                                          *"
	print "*         Connect PWMA to BCM27            *"
	print "*         Connect Ain1 to BCM17            *"
	print "*         Connect Ain2 to BCM22            *"
	print "*         Connect PWMB to BCM24            *"
	print "*         Connect Bin1 to BCM14            *"
	print "*         Connect Bin2 to BCM15            *"
	print "*                                          *"
	print "********************************************"
	GPIO.setmode(GPIO.BCM)
	GPIO.setup((17,27,22,14,15,24), GPIO.OUT)
	a = GPIO.PWM(27, 60)
	b = GPIO.PWM(24,60)

	a.start(0)
	b.start(0)
	

	def a_speed(value):
		a.ChangeDutyCycle(value)

	def a_bw_speed(value):
		a.ChangeDutyCycle(value)

	def b_speed(value):
		b.ChangeDutyCycle(value)

	delay = 0.05

	# CW MB, CCW MA
	print('CW MB, CCW MA')
	GPIO.output(17,0)
	GPIO.output(22,1)
	GPIO.output(15,0)
	GPIO.output(14,1)
	a.ChangeDutyCycle(10)
	b.ChangeDutyCycle(5)
	time.sleep(delay)
	a.ChangeDutyCycle(20)
	b.ChangeDutyCycle(10)
	time.sleep(delay)
	a.ChangeDutyCycle(30)
	b.ChangeDutyCycle(15)
	time.sleep(7)
	a.ChangeDutyCycle(0)
	b.ChangeDutyCycle(0)
	#for i in range(0,39):
	#	a.ChangeDutyCycle(i)
	#	time.sleep(delay)
	
	time.sleep(5)
	
	# CCW MB, CW MA
	print('CCW MB, CW MA')
	GPIO.output(22,0)
	GPIO.output(17,1)
	GPIO.output(14,0)
	GPIO.output(15,1)
	a.ChangeDutyCycle(10)
	b.ChangeDutyCycle(5)
	time.sleep(delay)
	a.ChangeDutyCycle(20)
	b.ChangeDutyCycle(10)
	time.sleep(delay)
	a.ChangeDutyCycle(30)
	b.ChangeDutyCycle(15)
	time.sleep(7)
	a.ChangeDutyCycle(0)
	b.ChangeDutyCycle(0)
	#for i in range(0,39):
	#	a.ChangeDutyCycle(i)
	#	time.sleep(delay)

	a.stop()
	b.stop()
	GPIO.cleanup()

	return

def destroy():
	a.stop()
	b.stop()
	GPIO.cleanup()

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		destroy()
