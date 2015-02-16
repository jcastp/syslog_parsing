#!/usr/bin/python3

# File used to store the functional tests of the application

import unittest
import socket

class func_test(unittest.TestCase):
    
    def setUp(self):
        self.serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.serversocket.bind(('localhost', 1514))
        self.serversocket.listen(5)
        return

    def test_socket_listens(self):
        """The socket must listen in the correct port."""
        return

    def test_message_is_not_empty(self):
        return

    def test_syslog_parse(self):
        return


    def tearDown(self):
        self.serversocket.close()
        return


if __name__ == "__main__":
    unittest.main()
