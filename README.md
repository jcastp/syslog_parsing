syslog_parsing
==============

Application taht opens a socket in a non-privileged port,
and listens to the redirected syslog.

Once it gets the syslog lines, it parses them, and inserts
the values into a database.