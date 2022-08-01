from .utils import network
from .data import Structs
from flask import Flask
from flask import render_template
from flask import request
from flask import Blueprint
import json

# Define this python file as the blueprint 
scanner = Blueprint('scanner', __name__) # __name__ is essentially the main() of this python file

@scanner.route('/')
def index():
    return "<h1>Go away, this isn't finished!</h1>"