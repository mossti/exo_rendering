from RPi import GPIO
from time import sleep

clk2 = 19 #B1
clk1 = 20 #A1
dt2 = 26 #B2
dt1 = 16 #A2

GPIO.setmode(GPIO.BCM)
GPIO.setup(clk1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(clk2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(dt1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(dt2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

counter1 = 0
counter2 = 0
clkLastState1 = GPIO.input(clk1)
clkLastState2 = GPIO.input(clk2)

try:

        while True:
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
                sleep(0.01)
finally:
        GPIO.cleanup()
        
if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		k = 1
                GPIO.cleanup()
		destroy()
