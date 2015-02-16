import re, parser

syslog_pattern = r'(\w{3}\s\d{2}\s\d{2}:\d{2}:\d{2})\s(\w+)\s([\/*|\w+|\-*]+)\[*(\d+)*\]*:\s(.*)'


def parsing_syslog(a_line):
    """Given a syslog line, we parse all of its components.
    """
    try:
        match = re.search(syslog_pattern, a_line)
        date, hostname, process, process_number, message = (match.group(1),
                                                          match.group(2),
                                                          match.group(3),
                                                          match.group(4),
                                                          match.group(5))

        # Convert to the mysql date format
        date = parser.time_convert(date)
        # If there is no process number, we convert it to -1
        if process_number is '' or process_number is None:
            process_number = -1
    except AttributeError:
        a_exception = a_line
        return (None, None, None, None, None), a_exception
                                                          
    return (date, hostname, process, process_number, message), None


