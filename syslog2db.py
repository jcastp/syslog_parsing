#!/usr/bin/python3

# Syslog receiver that parses the input and inserts the fields into a
# database 

import time, os, re
import socketserver
import syssocket.syslogsocket


def main(): 

    HOST='localhost'
    PORT=1514
    
    # We set a socket to listen to the syslog
    socketserver.TCPServer.allow_reuse_address = True
    server = syssocket.syslogsocket.MyTCPServer((HOST, PORT), syssocket.syslogsocket.MyTCPHandler)

    # Check database connection and tables
    server.db_connection()
    server.check_tables()
    

    server.serve_forever()


if __name__ == "__main__":
    main()
