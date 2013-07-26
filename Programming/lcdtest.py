#LCD Test (Hello World)
import sys
import os
import serial
import time

global serialport

#set up lcd on serial tx line
lcd = serial.Serial('/dev/ttyAMA0', 9600)
lcd.open()

#Write Happy Birthday to Jess
lcd.write('\xFE\x01') #clears screen
lcd.write('\xFE\x80') #sets on line 1, char 1
lcd.write(" Happy Birthday")
lcd.write('\xFE\xC0')
lcd.write("      Jess")
