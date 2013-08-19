import sys, serial, time
global serialport
LCD = serial.Serial('/dev/ttyAMA0', 9600)
LCD.open()

#updates the backlight
LCD.write('\x7C\x8C')

LCD.close()



