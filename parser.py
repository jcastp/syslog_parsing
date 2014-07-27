import re, time, datetime

pattern = r'(\w{3}\s\d{2}\s\d{2}:\d{2}:\d{2})\s(\w+)\s([\/*|\w+]+)\[*(\d+)*\]*:\s(.*)'

def time_convert(date):
    year = time.localtime()[0]
    date = str(year) + " " + date
    intermediate_date = datetime.datetime.strptime(date, "%Y %b %d %H:%M:%S")
    converted_date = intermediate_date.strftime("%Y-%m-%d %H:%M:%S")
    return converted_date


def parsing_syslog(a_line):
    """Given a syslog line, we parse all of its components.
    """
    match = re.search(pattern, a_line)
    date, hostname, process, process_number, message = (match.group(1),
                                                          match.group(2),
                                                          match.group(3),
                                                          match.group(4),
                                                          match.group(5))

    # Convert to the mysql date format
    date = time_convert(date)
    # If there is no process number, we convert it to -1
    if process_number is '' or process_number is None:
        process_number = -1
                                                          
    return date, hostname, process, process_number, message


def parse_audispd(message):
    """We need to parse the audispd messages"""
    # TODO
    return
