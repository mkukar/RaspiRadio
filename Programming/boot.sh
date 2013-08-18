#!/bin/bash
#Boot file to run when Rasberry Pi boots

#writes to LCD for easy SSH
python ~/RaspiRadio/Programming/writelcd.py 'Raspi Radio v1.0' 10.0.1.47

#Opens buttoncmd to enable front buttons
sudo python buttoncmd.py
