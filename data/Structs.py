from datetime import *

class Certificate():
    # Public Vars go here
    Common_Name = ""

    def __init__(self, cn):
        # TODO - Add more init vars here
        self.Common_Name = cn


# Object to encapsulate the endpoint
class Endpoint():
    URL = ""
    Port = ""
    IP = ""

    def __init__(self, url, port, frequency):
        self.URL = url
        self.Port = port
        self.Frequency = frequency

# Put Variables that won't change here
class Statics():
    STATIC_TEXT = "DONT CHANGE ME"