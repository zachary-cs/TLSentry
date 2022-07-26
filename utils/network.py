from OpenSSL import SSL
from cryptography import x509
from cryptography.x509.oid import NameOID
from socket import socket
from collections import namedtuple
import idna
from data import Structs


class SSL_Scanner():    
    
    def __init__(self, hostname, port):
        self.Endpoint = None
        self.Certificate = None
        self.Check_Certificate(hostname, port)
        
    def Verify_Cert(self, hostname):
        # verify notAfter/notBefore, CA trusted, servername/sni/hostname
        cert.has_expired()
        # service_identity.pyopenssl.verify_hostname(client_ssl, hostname)
        # issuer


    def Check_Certificate(self, hostname, port):
        idna_hostname = idna.encode(hostname)

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
        crypto_cert = cert.to_cryptography()
        # Close down
        sock_ssl.close()
        sock.close()

        # Setup the Certificate Object
        self.Certificate = Structs.Certificate(
                                    hostname,
                                    self.Get_Common_Name(crypto_cert), 
                                    peername,
                                    self.Get_Alt_Names(crypto_cert),
                                    self.Get_Issuer(crypto_cert),
                                    crypto_cert.not_valid_before,
                                    crypto_cert.not_valid_after
                                )

    # Helper Functions
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

