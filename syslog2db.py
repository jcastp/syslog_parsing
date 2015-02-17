#!/usr/bin/python3

# Syslog receiver that parses the input and inserts the fields into a
# database 

import time, os, re
import socketserver
import syssocket.syslogsocket
from sysparse import *
from db import *



def main():
    HOST='localhost'
    PORT=1514
    
    # We set a socket to listen to the syslog
    socketserver.TCPServer.allow_reuse_address = True
    server = socketserver.TCPServer((HOST, PORT), syssocket.syslogsocket.MyTCPHandler)

    server.serve_forever()


if __name__ == "__main__":
    main()








# Open a cursor to the database
#dbconn = db.connection()

# This reads the file each second, and get the new lines
# written 
#while 1:

        # TODO parse the line
#        parsed_line, exception = parser.parsing_syslog(line)
        # Insert the line into the database
        # Check if there is a exception in the parsing
#        if exception is not None:
#            db.insert_exception(dbconn, exception)
#        else:
#            db.insert_syslog(dbconn, parsed_line)
