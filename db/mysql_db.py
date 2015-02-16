# functions used to insert the syslog lines
# into the database

import MySQLdb

def connection():
    dbconn = MySQLdb.connect(host="localhost", user="syslogdb",
                        passwd="Sysl0gdb", db = "syslog")
                        
    return dbconn


def check_host(dbconn, hostname):
    """If the hostname is in the table, we get the id.
    If it's not, we insert it, and get the id.
    Anyway, we return the id.
    """
    cursor = dbconn.cursor()
    #Check presence
    sql_query = """SELECT * FROM hostname WHERE hostname = %s"""
    cursor.execute(sql_query, (hostname,))
    # If the hostname exists
    results = cursor.fetchone()
    if results is not None:
        id_number = results[0]
    else:
        sql_insert = """INSERT INTO hostname (hostname) VALUES (%s)"""
        cursor.execute(sql_insert, (hostname,))
        dbconn.commit()
        cursor.execute(sql_query, (hostname,))
        results = cursor.fetchone()
        id_number = results[0]
        
    cursor.close()

    return id_number


def check_process(dbconn, process):
    """If the process is in the table, we get the id.
    If it's not, we insert it, and get the id.
    Anyway, we return the id.
    """
    cursor = dbconn.cursor()
    #Check presence
    sql_query = """SELECT * FROM process WHERE process_name = %s"""
    cursor.execute(sql_query, (process,))
    # If the process exists
    results = cursor.fetchone()
    if results is not None:
        id_number = results[0]
    else:
        sql_insert = """INSERT INTO process (process_name) VALUES (%s)"""
        cursor.execute(sql_insert, (process,))
        dbconn.commit()
        cursor.execute(sql_query, (process,))
        results = cursor.fetchone()
        id_number = results[0]
        
    cursor.close()

    return id_number



def insert_exception(dbconn, exception):
    """If we couldnt parse the line correctly, we store
    the line into the exceptions table, so we can
    annalyze later what went wrong.
    """
    cursor = dbconn.cursor()
    sql_sentence = """INSERT INTO exceptions (data) VALUES (%s)"""
    cursor.execute(sql_sentence, (exception,))
    dbconn.commit()
    cursor.close()
    return


def insert_syslog(dbconn, parsed_line):
    """Once the line has been parsed, we insert the values
    into the database.
    """
    cursor = dbconn.cursor()
    date, hostname, process, process_number, message = parsed_line
    # Check if the hostname is already in the database
    host_id = check_host(dbconn, hostname)
    # Check if the process is already in the database
    proc_id = check_process(dbconn, process)

    sql_insert = """INSERT INTO syslog (date, host_id, proc_id, proc_number, message) VALUES (%s, %s, %s, %s, %s)"""

    cursor.execute(sql_insert, (date, host_id, proc_id, process_number, message))
    dbconn.commit()
    
    cursor.close()
    return
