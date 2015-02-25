import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
import pymysql
from sqlalchemy.orm import sessionmaker


Base = declarative_base()

class Hostname(Base):
    __tablename__ = "hostname"

    id = Column(Integer, primary_key=True)
    hostname = Column(String(50))
    
    def __repr__(self):
        return "Hostname({0})".format(self.hostname)


class Process(Base):
    __tablename__ = "process"
    
    id = Column(Integer, primary_key=True)
    process = Column(String(50))
    
    def __repr__(self):
        return "Process({0})".format(self.process)



class Log(Base):
    __tablename__ = "log"

    id = Column(Integer, primary_key=True)
    date = Column(DateTime)
    host = Column(Integer, ForeignKey('hostname.id'))
    process = Column(Integer, ForeignKey('process.id'))
    message = Column(String(2000))



def create_db_connection():
    engine = sqlalchemy.create_engine('mysql+pymysql://syslogdb:Sysl0gdb@localhost/syslog', echo = True)
    return engine


def check_or_create_tables(engine, base):
    base.metadata.create_all(engine)
    return


def check_host(session, host):
    """
    """
    # Query the database searching for the hostname
    result = session.query(Hostname.hostname, Hostname.id).filter(Hostname.hostname == host)
    # If the host exists, we return the ID of the host
    if result.first() is not None:
        return result.first()[1]
    else:
        host_to_add = Hostname(hostname = host)
        session.add(host_to_add)
        session.commit()
        result = session.query(Hostname.hostname, Hostname.id).filter(Hostname.hostname == host)
        return result.first()[1]


def check_process(session, proc):
    # Query the database searching for the process
    result = session.query(Process.process, Process.id).filter(Process.process == proc)
    # If the proc exists, we return the ID of the host
    if result.first() is not None:
        return result.first()[1]
    else:
        proc_to_add = Process(process = proc)
        session.add(proc_to_add)
        session.commit()
        result = session.query(Process.process, Process.id).filter(Process.process == proc)
        return result.first()[1]


def insert_data(engine, data):
    Session = sessionmaker(bind=engine)
    session = Session()
    date1, host1, proc1, procnum1, message1 = data
    host_id = check_host(session, host1)
    proc_id = check_process(session, proc1)

    log_to_add = Log(date = date1, host = host_id, process = proc_id,
                     message = message1)
    session.add(log_to_add)
    session.commit()
    
    return
