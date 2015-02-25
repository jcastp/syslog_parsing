import socketserver
import sysparse.libparser
import sysdb.dbfunctions



class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    The RequestHandler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """



    def handle(self):
        """This is the main function of the application, and this
        is where the data is going to be processed
        """
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        if self.data != "":
            print(self.data)
            # Clean the data received to get a clean line of text
            text = sysparse.libparser.clean_message(self.data)
            # Check the origin of the line (sylog, audit, etc)
            kind = (sysparse.libparser.classify_lines(text))
            # Parse it
            data, exception = sysparse.libparser.parse(kind, text)
            # Add it to the database
            print(data)
            sysdb.dbfunctions.insert_data(self.server.engine, data)

            
            
