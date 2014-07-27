# Program to read the syslog line by line, as it is updated
# and extract all the information to insert it into a database
# We have to parse the syslog and the auditd messages, to
# insert them into the database

import time, os, re
import parser
import db


#Set the filename and open the file
filename = '/var/log/syslog'
file = open(filename,'r')


#Find the size of the file and move to the end
st_results = os.stat(filename)
st_size = st_results[6]
file.seek(st_size)

# Open a cursor to the database
dbconn = db.connection()

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
        parsed_line, exception = parser.parsing_syslog(line)
        print parsed_line
        # Insert the line into the database
        # Check if there is a exception in the parsing
        if exception is not None:
            db.insert_exception(dbconn, exception)
        else:
            db.insert_syslog(dbconn, parsed_line)

