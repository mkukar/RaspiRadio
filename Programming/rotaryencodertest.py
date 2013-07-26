#GPIO Rotary Encoder Test (Button and Knob)

import RPi.GPIO as GPIO
import os
import time

#Uses default board setup
GPIO.setmode(GPIO.BCM)

#Button Input
GPIO.setup(11, GPIO.IN)
#Rotary Encoder Input (A = 10, B = 9)
GPIO.setup(10, GPIO.IN)
GPIO.setup(9, GPIO.IN)

#Rotary Encoder Values
position = 0 #starts position at 0 (goes up or down)
oldA = GPIO.input(10) #old state of rotA

#Reads value from GPIO and writes output
while True:
	#Checks if button is pressed
	if (GPIO.input(11)):
		os.system("echo Button Pressed")

	#Checks if encoder changed state
	rotA = GPIO.input(10)
	rotB = GPIO.input(9)
	if ((rotA == True) and (oldA == False)): #detects when rotA goes high (peaks)	
		if (rotB == False):
			#Clockwise
			position += 1
		else:
			#Counterclockwise
			position -= 1
		#Writes out new position
		os.system("echo " + str(position))
	oldA = rotA #sets them equal to prevent overlap of reading
