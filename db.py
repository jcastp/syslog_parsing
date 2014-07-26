# functions used to insert the syslog lines
# into the database

import MySQLdb

def connection():
    db = MySQLdb.connect(host="localhost", user="syslogdb",
                        passwd="Sysl0gdb", db = "syslog")
                        
    c = db.cursor()
    return c


