#!/usr/bin/python3

# File used to store the functional tests of the application

import unittest
import syssocket.syslogsocket
import socketserver

class func_test(unittest.TestCase):
    
    def setUp(self):
        return

    def test_socket_listens(self):
        """The socket must listen in the correct port."""
        return

    def test_message_is_not_empty(self):
        return

    def test_syslog_parse(self):
        return


    def tearDown(self):

        return


if __name__ == "__main__":
    unittest.main()
