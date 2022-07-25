from datetime import *
from OpenSSL import SSL

# Object to encapsulate the endpoint
class Endpoint():

    def __init__(self, url, port):
        self.URL = url
        self.Port = port

# Put Variables that won't change here
class Statics():
    STATIC_TEXT = "DONT CHANGE ME"