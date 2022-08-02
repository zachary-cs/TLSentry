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
def index(name=None):
  pagedata = Structs.PageData()
  return render_template('home_index.j2', pagedata=pagedata)
