#!/bin/bash

#Switches between Pianobar and the time display

#Checks if pianobar is running
ps -C 'pianobar' > /dev/null

#If it is not running, open pianobar
if [ $? -ne 0 ]; then
	#Shows opening prompt
	python /home/pi/RaspiRadio/Programming/writelcd.py "OPENING" "PIANOBAR"
	pianobar;
	#QUIT TIME DISPLAY SCRIPT HERE
	exit 1;
fi

#Otherwise first quit pianobar
echo 'q' >> /home/pi/.config/pianobar/ctl
python /home/pi/RaspiRadio/Programming/writelcd.py "CLOSING" "PIANOBAR"

#then open time display script

#TIME DISPLAY SCRIPT GOES HERE
