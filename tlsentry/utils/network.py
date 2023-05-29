from OpenSSL import SSL
from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives import serialization
from socket import socket
import idna
import hashlib
from ..data import Structs



class Scanner():   

    def __init__(self, hostname, port):

        # Public Vars
        self.Certificate = None
        self.Endpoint = None
        self.PEM_Cert = None

        # Pull the SSL Cert from the Hostname:Port
        self.ScanHost(hostname, port)

    def ScanHost(self, hostname, port):
        idna_hostname = idna.encode(hostname)

        # TODO - Better error handling for bad hostname/ports

        # Setup socket connection
        sock = socket()
        sock.connect((hostname, port))
        peername = sock.getpeername()
        ctx = SSL.Context(SSL.SSLv23_METHOD)
        ctx.check_hostname = False
        ctx.verify_mode = SSL.VERIFY_NONE
        # Do Handshake and acquire Cert
        sock_ssl = SSL.Connection(ctx, sock)
        sock_ssl.set_connect_state()
        sock_ssl.set_tlsext_host_name(idna_hostname)
        sock_ssl.do_handshake()
        cert = sock_ssl.get_peer_certificate()
        
        # Check for null cert
        if cert is None:
            return
        else:
            crypto_cert = cert.to_cryptography()
            # Close down
            sock_ssl.close()
            sock.close()

        
        # Save obtained cert objects
        self.Cert = cert
        self.CryptoCert = crypto_cert
        self.PEM_Cert = crypto_cert.public_bytes(serialization.Encoding.PEM).decode()

        # Generate the Fingerprint of the Certificate
        PEM_Data = self.PEM_Cert.replace("-----BEGIN CERTIFICATE-----\n","")
        PEM_Data = PEM_Data.replace("-----END CERTIFICATE-----\n","")
        PEM_Data = PEM_Data.replace("\n","")
        fingerprint = hashlib.sha1(self.PEM_Cert.encode('utf-8')).hexdigest() 

        # Setup the Certificate Object
        self.Certificate = Structs.Certificate(
                                    hostname,
                                    self.Get_Common_Name(crypto_cert), 
                                    peername,
                                    self.Get_Alt_Names(crypto_cert),
                                    self.Get_Issuer(crypto_cert),
                                    crypto_cert.not_valid_before,
                                    crypto_cert.not_valid_after,
                                    fingerprint
                                )
        # Setup the Endpoint Object
        self.Endpoint = Structs.Endpoint(hostname, port, peername[0])


    # Helper Functions        
    def Get_Certificate(self):
        return self.Certificate
        
    def Verify_Cert(self, hostname):
        # verify notAfter/notBefore, CA trusted, servername/sni/hostname
        cert.has_expired()
        # service_identity.pyopenssl.verify_hostname(client_ssl, hostname)
        # issuer

    def Get_Alt_Names(self, cert):
        try:
            ext = cert.extensions.get_extension_for_class(x509.SubjectAlternativeName)
            return ext.value.get_values_for_type(x509.DNSName)
        except x509.ExtensionNotFound:
            return None

    def Get_Common_Name(self, cert):
        try:
            names = cert.subject.get_attributes_for_oid(NameOID.COMMON_NAME)
            return names[0].value
        except x509.ExtensionNotFound:
            return None

    def Get_Issuer(self, cert):
        try:
            names = cert.issuer.get_attributes_for_oid(NameOID.COMMON_NAME)
            return names[0].value
        except x509.ExtensionNotFound:
            return None

