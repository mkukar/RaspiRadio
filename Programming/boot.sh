#!/bin/bash
#Boot file to run when Rasberry Pi boots

#writes to LCD
python ~/RaspiRadio/Programming/writelcd.py 'Raspi Radio' v1.0

#opens pianobar
pianobar
