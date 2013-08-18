#Uses front buttons to control Raspi Radio

import RPi.GPIO as GPIO
import os
import time

#uses default board setup (pins marked by P1 header)
GPIO.setmode(GPIO.BOARD)

#Sets up buttons as input
GPIO.setup(22, GPIO.IN) #LEFT
GPIO.setup(23, GPIO.IN) #RIGHT

#Reads value from GPIO on infinite loop (run this program in the background)
while True:
	if (GPIO.input(22)):
		if (GPIO.input(23)):
			os.system("python /home/pi/RaspiRadio/Programming/writelcd.py SHUTTING DOWN")
			os.system("echo SHUTDOWN CMD HERE")
		else:
			os.system("echo 'p' >> /home/pi/.config/pianobar/ctl")
	elif (GPIO.input(23)):
		if (GPIO.input(22)):
			os.system("echo /home/pi/RaspiRadio/Programming/writelcd.py SHUTTING DOWN")
			#shutdown cmd here
		else:
			os.system("bash /home/pi/RaspiRadio/Programming/pianobarpwr.sh")
	time.sleep(0.1)
