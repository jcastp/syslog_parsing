#!/usr/bin/python3

# Syslog receiver that parses the input and inserts the fields into a
# database 

import time, os, re
import socketserver
from parser import *
import db
from syssocket import *



HOST='localhost'
PORT=1514

# We set a socket to listen to the syslog
socketserver.TCPServer.allow_reuse_address = True
server = socketserver.TCPServer((HOST, PORT), syslogsocket.MyTCPHandler)

server.serve_forever()





# Read what is sento to the syslog
#while True:
    # accept connections from outside
#    (clientsocket, address) = serversocket.accept()
    # now do something with the clientsocket
    # The socket gets the output of the syslog
#    message = clientsocket.recv(4096)
# TODO
#    if message:
#        print(message)
        # Separate the different lines received
#        text = message.decode("utf-8")
#        print(text)
        # Identify the syslog received (syslog, auditd, etc)
        # Parse the line, according the type
        # Insert into the database


#    clientsocket.close()

#serversocket.close()












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
