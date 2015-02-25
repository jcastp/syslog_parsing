import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
import pymysql


def create_db_connection():
    engine = sqlalchemy.create_engine('mysql+pymysql://syslogdb:Sysl0gdb@localhost/syslog', echo = True)
    return engine


def check_or_create_tables(engine):
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


    # TODO crear el resto de tablas

    class Log(Base):
        __tablename__ = "log"

        id = Column(Integer, primary_key=True)
        date = Column(DateTime)
        host = Column(Integer, ForeignKey('hostname.id'))
        process = Column(Integer, ForeignKey('process.id'))
        message = Column(String(2000))

    Base.metadata.create_all(engine)

    return


def check_host():
    return

def check_process():
    return



def insert_data():
    return
