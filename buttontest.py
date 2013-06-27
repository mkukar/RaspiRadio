#GPIO Button In Test

import RPi.GPIO as GPIO
import os
import time

#Uses default board setup
GPIO.setmode(GPIO.BCM)

#Sets pin 11 as input
GPIO.setup(11, GPIO.IN)

#Reads value from GPIO and writes output
while True:
	if (GPIO.input(11)):
		os.system("echo PRESSED")
	time.sleep(0.1)
