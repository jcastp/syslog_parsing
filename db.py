# functions used to insert the syslog lines
# into the database

import MySQLdb

def connection():
    dbconn = MySQLdb.connect(host="localhost", user="syslogdb",
                        passwd="Sysl0gdb", db = "syslog")
                        
    c = dbconn.cursor()
    return dbconn, c


def insert_exception(cursor, exception):
    """If we couldnt parse the line correctly, we store
    the line into the exceptions table, so we can
    annalyze later what went wrong.
    """
    sql_sentence = """INSERT INTO exceptions (data)
VALUES (%s)"""
    cursor.execute(sql_sentence, (exception,))
    return


def insert_syslog(cursor, parsed_line):
    return
