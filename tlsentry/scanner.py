from .utils import network
from .data import Structs
from flask import Flask
from flask import render_template
from flask import request
from flask import Blueprint
import json

# Define this python file as the blueprint 
scanner = Blueprint('scanner', __name__) # __name__ is essentially the main() of this python file


# This code will end up being the API, for which can be called to scan endpoints

# TODO Scanning API
@scanner.route('/scan', methods=['POST','GET'])
def scan_urls():
  if request.method == 'POST':
    # TODO
    return ""
  else:
    scanner = network.SSL_Scanner("www.google.com", 443)
    # Get Dict object of Certificate
    cert_dict = scanner.Certificate.GetDict()
    return json.dumps(cert_dict)



@scanner.route('/')
def index():
    return "<h1>Go away, this isn't finished!</h1>"