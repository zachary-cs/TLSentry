from flask import Flask
from flask import render_template
from flask import request
from flask import Blueprint
from .utils import network
from .data import Structs


# Define this python file as the blueprint 
endpoints = Blueprint('endpoints', __name__) # __name__ is essentially the main() of this python file

# Index of endpoints
@endpoints.route("/")
def index():
  page_data = Structs.PageData()
  return render_template('endpoints_index.j2', pagedata=page_data)


