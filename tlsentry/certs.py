from flask import Flask
from flask import render_template
from flask import request
from flask import Blueprint
from .utils import network
from .data import Structs


# Define this python file as the blueprint 
certs = Blueprint('certs', __name__) # __name__ is essentially the main() of this python file

# Index of Certs
@certs.route("/")
def index():
  pagedata = Structs.PageData()
  return render_template('certs_index.j2', pagedata=pagedata)


