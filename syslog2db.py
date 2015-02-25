#!/usr/bin/python3

# Syslog receiver that parses the input and inserts the fields into a
# database 

import time, os, re
import socketserver
import syssocket.syslogsocket
import sysdb.dbfunctions


def main(): 

    HOST='localhost'
    PORT=1514
    
    # We set a socket to listen to the syslog
    socketserver.TCPServer.allow_reuse_address = True
    server = socketserver.TCPServer((HOST, PORT), syssocket.syslogsocket.MyTCPHandler)
    
    # Create a connection against the database
    engine = sysdb.dbfunctions.create_db_connection()
    sysdb.dbfunctions.check_or_create_tables(engine, sysdb.dbfunctions.Base)
    # Using this trick to pass the connection to the handler
    server.engine = engine

    server.serve_forever()


if __name__ == "__main__":
    main()
