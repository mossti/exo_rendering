
import time
import numpy as np
import RPi.GPIO as GPIO

# Three-wire SSI for AEAT-601012
# (#1) CS = 0, DO = 1, CLK = 3
# (#2) CS = 5, DO = 6, CLK = 7

def ssi_init():
	GPIO.output(0,1)
	GPIO.output(3,1)
	GPIO.output(5,1)
	GPIO.output(7,1)

def start_read():
	GPIO.output(0,0)
	GPIO.output(5,0)
	a = GPIO.input(1)
	b = GPIO.input(6)
	print(a)
	print(b)
	time.sleep(0.0000001)
	a = GPIO.input(1)
	b = GPIO.input(6)
	print(a)
	print(b)
	time.sleep(0.0000004)
	a = GPIO.input(1)
	b = GPIO.input(6)
	print(a)
	print(b)
	GPIO.output(3,0)
	GPIO.output(7,0)
	a = GPIO.input(1)
	b = GPIO.input(6)
	print(a)
	print(b)
	return

def main():
	import time
	global k
	k = 0
	
	GPIO.setmode(GPIO.BCM)
	GPIO.setup((0,3), GPIO.OUT)
	GPIO.setup((5,7), GPIO.OUT)
	GPIO.setup(1,GPIO.IN)
	GPIO.setup(6,GPIO.IN)
	
	ssi_init()
	
	time.sleep(0.2)
	
	while k != 1: 
		entry = np.array([0])
		
		ssi_init()
		
		time.sleep(0.0000005)
		
		start_read()
		
		time.sleep(5/1000000.0)
		
		for i in range(0,12):
			
			GPIO.output(3,1)
			GPIO.output(7,1)
			
			time.sleep(0.000000375)
			
			a = GPIO.input(1)
			b = GPIO.input(6)
			
			time.sleep(0.000000125)
			
			GPIO.output(3,0)
			GPIO.output(7,0)
			
			time.sleep(0.0000005)
			
			if i == 0:
				#entry[0] = a
				entry_a = str(a)
				entry_b = str(b)
			else:
				#entry = np.append(entry, a)
				entry_a = entry_a + str(a)
				entry_b = entry_b + str(b)
				
			
		#entry = np.array2string(entry)
		entry_a = int(entry_a,2)
		entry_b = int(entry_b,2)
		
		print(entry_a)
		print(entry_b)
	
	return
	
def destroy():
	GPIO.cleanup()

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		k = 1
		destroy()
