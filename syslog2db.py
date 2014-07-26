# Program to read the syslog line by line, as it is updated
# and extract all the information to insert it into a database
# We have to parse the syslog and the auditd messages, to
# insert them into the database

import time, os, re


#Set the filename and open the file
filename = '/var/log/syslog'
file = open(filename,'r')


#Find the size of the file and move to the end
st_results = os.stat(filename)
st_size = st_results[6]
file.seek(st_size)


# This reads the file each second, and get the new lines
# written 
while 1:
    where = file.tell()
    line = file.readline()
    if not line:
        time.sleep(1)
        file.seek(where)
    else:
        # TODO parse the line
        print line, # already has newline

