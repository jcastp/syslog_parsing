# Generic functions used by all the parsers

import time, datetime
import sysparse.syslog_parser
import sysparse.audit_parser

def time_convert(date):
    year = time.localtime()[0]
    date = str(year) + " " + date
    intermediate_date = datetime.datetime.strptime(date, "%Y %b %d %H:%M:%S")
    converted_date = intermediate_date.strftime("%Y-%m-%d %H:%M:%S")
    return converted_date


def clean_message(bytes_object):
    """Gets a bytes object and, converts it to string, divides it by new line
    and ..."""
    text = bytes_object.decode("utf-8")
    # Get rid of the "<nn> header, thst is not interesting for 
    ## our purposes
    text = text[text.find('>') + 1:]
    return text


def classify_lines(message):
    """Given a text line, detect what kind of event it is, to classify it."""
    if message.startswith('type'):
        return "audit"
    # TODO modify this to ascertain if it is a syslog entry
    else:
        return "syslog"
    return


def parse(kind, text):
    """Once given the type of log received, and the line text, it launches
    the correct parsing functions"""
    if kind == "syslog":
        return sysparse.syslog_parser.parsing_syslog(text)
    elif kind == "audit":
        return None
    return
