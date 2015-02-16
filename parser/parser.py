# Generic functions used by all the parsers

import time, datetime

def time_convert(date):
    year = time.localtime()[0]
    date = str(year) + " " + date
    intermediate_date = datetime.datetime.strptime(date, "%Y %b %d %H:%M:%S")
    converted_date = intermediate_date.strftime("%Y-%m-%d %H:%M:%S")
    return converted_date


def separate_syslog_lines(message):
    return
