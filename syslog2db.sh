#! /bin/bash
### BEGIN INIT INFO
# Provides:          syslogdb
# Required-Start:    $rsyslog
# Required-Stop:     $rsyslog
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description  syslog to db
# Description:       
### END INIT INFO

PATH="/root/syslog_parsing/"
EXECUTABLE="syslog2db.py"

case "$1" in
    start)
	/usr/bin/python ${PATH}${EXECUTABLE} &
	;;
    stop)
	;;
    status)
	/bin/ps aux | /bin/grep ${EXECUTABLE}
	;;
esac