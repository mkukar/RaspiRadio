#!/bin/bash

### BEGIN INIT INFO
# Provides:          RaspiRadio_Boot
# Required-Start:    $remote_fs $syslog
# Required-Stop:     $remote_fs $syslog
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description: Sets up RaspiRadio at boot
# Description:       Simple script that sets up the RaspiRadio at boot
### END INIT INFO

#MOVE THIS FILE TO /etc/rc.local

#writes to LCD for easy SSH
python ~/RaspiRadio/Programming/writelcd.py 'Raspi Radio v1.0' 10.0.1.47

#Opens buttoncmd to enable front buttons
sudo python ~/RaspiRadio/Programming/buttoncmd.py &
