from .utils import network
from .data import Structs
from flask import Flask
from flask import render_template
from flask import request
from flask import Blueprint
import json

# Define this python file as the blueprint 
home = Blueprint('home', __name__) # __name__ is essentially the main() of this python file

@home.get("/")
@home.get("/index.html")
def index(name=None):
  page_data = {
    'title' : "TLSentry - Endpoint SSL Monitoring",
    'test' : 123
  }
  return render_template('home_index.j2', title=page_data["title"])





# TODO Scanning API
@home.route('/scan', methods=['POST','GET'])
def scan_urls():
  if request.method == 'POST':
    # TODO
    return ""
  else:
    scanner = network.SSL_Scanner("www.google.com", 443)
    # Get Dict object of Certificate
    cert_dict = scanner.Certificate.GetDict()
    return json.dumps(cert_dict)


