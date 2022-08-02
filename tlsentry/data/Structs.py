from datetime import *
from OpenSSL import SSL



class PageData():
    # Public Static Vars
    app_version = 0.1
    title = "TLSentry - Endpoint SSL Monitoring"

    def __init__(self):
        pass

class Certificate():

    def __init__(self, hostname, commonname, peername, san, issuer, notbefore, notafter):
        self.Hostname = hostname
        self.CN = commonname
        self.PeerName = peername
        self.SAN = san
        self.Issuer = issuer
        self.NotBefore = notbefore
        self.NotAfter = notafter

    def GetDict(self):
        return {
            "Hostname": self.Hostname,
            "Common Name": self.CN,
            "Peer Name": self.PeerName,
            "SAN": self.SAN,
            "Issuer" : self.Issuer,
            "Not Valid Before": str(self.NotBefore),
            "Not Valid After": str(self.NotAfter)
        }


# Object to encapsulate the endpoint
class Endpoint():

    def __init__(self, url, port):
        self.URL = url
        self.Port = port

# Put Variables that won't change here
class Statics():
    STATIC_TEXT = "DONT CHANGE ME"