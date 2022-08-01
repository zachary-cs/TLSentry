from flask import Flask
from flask import render_template
from flask import request
from flask import Blueprint
from .utils import network
from .data import Structs


# Define this python file as the blueprint 
snips = Blueprint('snips', __name__) # __name__ is essentially the main() of this python file



# Basic Var capture - GET on /hello/
@snips.route("/hello/")
@snips.route("/hello/<name>")
def hello(name):
  return render_template('hello.j2',name=name)



# ======================== Code Testing =========================


# Testing out returning JSON from a URL
@snips.route("/json")
def json_test():
  return json.dumps({"Test" : 50})



