from flask import Flask
from flask import render_template
from flask import request
from flask import Blueprint
from .utils import network
from .data import Structs
import json
import hashlib

# Define this python file as the blueprint 
snips = Blueprint('snips', __name__) # __name__ is essentially the main() of this python file



# Basic Var capture - GET on /hello/
@snips.route("/hello/")
@snips.route("/hello/<name>")
def hello(name):
  return render_template('hello.html',name=name)



# ======================== Code Testing =========================

@snips.route("/cert")
def cert_get():
  scanner = network.Scanner("google.com", 443)
  cert = scanner.Certificate
  return json.dumps(
                      {
                        "Test" : 50, 
                        "Test2": 100,
                        "Cert" : cert.GetDict(),
                        "Endpoint" : scanner.Endpoint.GetDict()                    
                      }
                    )

@snips.route("/thumb")
def thumb():
  scanner = network.Scanner("google.com", 443)
  cert = scanner.Cert
  crypto_cert = scanner.CryptoCert
  certificate = scanner.Certificate
  return json.dumps(
                      {
                        # "Thumbprint" : certificate.Thumbprint
                        # "Cert" : dir(cert),
                        "Crypto_Cert" : dir(crypto_cert),
                        "PEM" : scanner.PEM_Cert,
                        "SHA1 Fingerprint" : certificate.Fingerprint
                        # "Bytes" : cert.public_bytes("utf")
                      }
                    )


# Testing out returning JSON from a URL
@snips.route("/json")
def json_test():
  return json.dumps({"Test" : 50})



