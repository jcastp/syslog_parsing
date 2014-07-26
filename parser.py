import re

pattern = r'(\w{3}\s\d{2}\s\d{2}:\d{2}:\d{2})\s(\w+)\s(\w+/*\w+\[*(\d*)*\]*):\s(.*)'


def parsing_syslog(a_line):
    """Given a syslog line, we parse all of its components.
    """
    match = re.search(pattern, a_line)
    (date, hostname, process, process_number, message) = (match.group(1),
                                                          match.group(2),
                                                          match.group(3),
                                                          match.group(4),
                                                          match.group(5))
    print date
    print hostname
    print process
    print process_number
    print message
    return


def parse_audispd(message):
    """We need to parse the audispd messages""".
    return
