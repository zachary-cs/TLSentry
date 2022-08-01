from .utils import network
from .data import Structs
from flask import Flask
from flask import render_template
from flask import request
from flask import Blueprint
import mysql.connector
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
  return render_template('index.j2', title=page_data["title"])

# Basic Var capture - GET on /hello/
@home.route("/hello/")
@home.route("/hello/<name>")
def hello(name):
  return render_template('hello.j2',name=name)





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


# Routing for Static files, answered by:
# https://stackoverflow.com/questions/30011170/flask-application-how-to-link-a-javascript-file-to-website











# ======================== Code Testing =========================


# Testing out returning JSON from a URL
@home.route("/json")
def json_test():
  return json.dumps({"Test" : 50})





# ======================== SQL Tutorial Stuff =========================

@home.route('/widgets')
def get_widgets():
  mydb = mysql.connector.connect(
    host="mysqldb",
    user="root",
    password="p@ssw0rd1",
    database="inventory"
  )
  cursor = mydb.cursor()


  cursor.execute("SELECT * FROM widgets")

  row_headers=[x[0] for x in cursor.description] #this will extract row headers

  results = cursor.fetchall()
  json_data=[]
  for result in results:
    json_data.append(dict(zip(row_headers,result)))

  cursor.close()

  return json.dumps(json_data)

@home.route('/initdb')
def db_init():
  mydb = mysql.connector.connect(
    host="mysqldb",
    user="root",
    password="p@ssw0rd1"
  )
  cursor = mydb.cursor()

  cursor.execute("DROP DATABASE IF EXISTS inventory")
  cursor.execute("CREATE DATABASE inventory")
  cursor.close()

  mydb = mysql.connector.connect(
    host="mysqldb",
    user="root",
    password="p@ssw0rd1",
    database="inventory"
  )
  cursor = mydb.cursor()

  cursor.execute("DROP TABLE IF EXISTS widgets")
  cursor.execute("CREATE TABLE widgets (name VARCHAR(255), description VARCHAR(255))")
  cursor.close()

  return 'init database'

if __name__ == "__main__":
  app.run(host ='0.0.0.0')