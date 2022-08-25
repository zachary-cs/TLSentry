from datetime import *
from OpenSSL import SSL



class PageData():
    # Public Static Vars
    app_version = 0.1
    title = "TLSentry - Endpoint SSL Monitoring"
    def __init__(self):
        pass

class Certificate():

    def __init__(self, hostname, commonname, peername, san, issuer, notbefore, notafter, thumbprint="TESTTHUMBPRINT"):
        self.Hostname = hostname
        self.CommonName = commonname
        self.PeerName = peername
        self.SAN = san
        self.Issuer = issuer
        self.NotBefore = notbefore
        self.NotAfter = notafter
        self.Thumbprint = thumbprint

    def GetDict(self):
        return {
            "Hostname": self.Hostname,
            "Common Name": self.CommonName,
            "Peer Name": self.PeerName,
            "SAN": self.SAN,
            "Issuer" : self.Issuer,
            "Not Valid Before": str(self.NotBefore),
            "Not Valid After": str(self.NotAfter),
            "Thumbprint": self.Thumbprint
        }


# Object to encapsulate the endpoint
class Endpoint():

    def __init__(self, url, port):
        self.URL = url
        self.Port = port

# Put Variables that won't change here
class Statics():
    STATIC_TEXT = "DONT CHANGE ME"