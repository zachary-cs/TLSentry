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
        self.check_certificate(hostname, port)
        
    def verify_cert(self, cert, hostname):
        # verify notAfter/notBefore, CA trusted, servername/sni/hostname
        cert.has_expired()
        # service_identity.pyopenssl.verify_hostname(client_ssl, hostname)
        # issuer


    def check_certificate(self, hostname, port):
        hostname_idna = idna.encode(hostname)

        sock = socket()
        sock.connect((hostname, port))
        peername = sock.getpeername()
        ctx = SSL.Context(SSL.SSLv23_METHOD)
        ctx.check_hostname = False
        ctx.verify_mode = SSL.VERIFY_NONE

        sock_ssl = SSL.Connection(ctx, sock)
        sock_ssl.set_connect_state()
        sock_ssl.set_tlsext_host_name(hostname_idna)
        sock_ssl.do_handshake()
        cert = sock_ssl.get_peer_certificate()
        crypto_cert = cert.to_cryptography()
        sock_ssl.close()
        sock.close()

        self.Certificate = Structs.Certificate(
                                    hostname,
                                    self.get_common_name(crypto_cert), 
                                    peername,
                                    self.get_alt_names(crypto_cert),
                                    self.get_issuer(crypto_cert),
                                    crypto_cert.not_valid_before,
                                    crypto_cert.not_valid_after
                                )


    def get_alt_names(self, cert):
        try:
            ext = cert.extensions.get_extension_for_class(x509.SubjectAlternativeName)
            return ext.value.get_values_for_type(x509.DNSName)
        except x509.ExtensionNotFound:
            return None

    def get_common_name(self, cert):
        try:
            names = cert.subject.get_attributes_for_oid(NameOID.COMMON_NAME)
            return names[0].value
        except x509.ExtensionNotFound:
            return None

    def get_issuer(self, cert):
        try:
            names = cert.issuer.get_attributes_for_oid(NameOID.COMMON_NAME)
            return names[0].value
        except x509.ExtensionNotFound:
            return None

    def check_it_out(self, hostname, port):
        hostinfo = get_certificate(hostname, port)
        print_basic_info(hostinfo)

