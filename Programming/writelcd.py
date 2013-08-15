import sys, serial, time
global serialport
LCD = serial.Serial('/dev/ttyAMA0', 9600)
LCD.open()
#Clears the display
LCD.write('\xFE\x01')

#Checks if there are two line arguments, or else it displays nothing

if len(sys.argv) != 3:
	LCD.close()

else:
	#First line
	LCD.write('\xFE\x80')
	
	#checks length, if longer than 16 it appends it with ',,,'
	if len(str(sys.argv[1])) > 16:
		LCD.write(str(sys.argv[1])[0:13] + '...')
	else:
		#centers the screen by adding spaces to each side until the string length is 16 characters
		topLine = str(sys.argv[1])
		switch = 0
		while len(topLine) < 16:
			if switch == 0:
				switch = 1
				topLine = ' ' + topLine
			else:
				switch = 0
				topLine = topLine + ' '
		LCD.write(topLine)

	#Second line
	LCD.write('\xFE\xC0')
	
	#checks length, if longer than 16 it appends it with '...'
	if len(str(sys.argv[2])) > 16:
		LCD.write(str(sys.argv[2])[0:13] + '...')
	else:
		#centers the screen by adding spaces to each side until the string length is 16 characters
		bottomLine = str(sys.argv[2])
		switch = 0
		while len(bottomLine) < 16:
			if switch == 0:
				bottomLine = ' ' + bottomLine
				switch = 1
			else:
				bottomLine = bottomLine + ' '
				switch = 0
		LCD.write(bottomLine)

	LCD.close()
