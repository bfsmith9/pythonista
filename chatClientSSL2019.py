#! /usr/bin/env python

"""
*** Barry Smith - CS265 - April 17, 2017 ***

NOTICE: THIS PROGRAM IS WRITTEN IN PYTHON 2! 
"""

import socket
import re
import time
import struct
import ssl

from chat_client import chat_client

class chat_clientSSL(chat_client):
    """
    chat_clientSSL extends chat_client class, adding SSL functionality
    """

    # chat_clientSSL methods
    def __init__(self):
        # print("Initialized")
        True

    def clientConnectSSL(self, host, port):
        """ connects to host using SSL """

        ctx = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
        ctx.verify_mode = ssl.CERT_REQUIRED

        s = ctx.wrap_socket(socket.socket())


        try:
            s.connect((host, port))
            # Have to decode in p3 b/c comes back as bytes, not string
            # print(chatSocketrecv(1024).decode("utf-8"))
            self.initialServerResponse = (s.recv(1024).decode("utf-8"))
            print(self.initialServerResponse.rstrip())
            if (self.initialServerResponse == "HELLO\n"):
                print("Server responded!")
            # Able to return socket!
            return s
        except ssl.SSLError:
            print("SSL Certification Fail")
            print("Please talk to your system administrator or "
                  "try a different port.\n")
            
# End chat_clientSSL
