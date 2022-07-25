from utils import network
from data import Structs
from flask import Flask
from flask import render_template
import mysql.connector
import json


app = Flask(__name__)


@app.get("/")
def index(name=None):
    return render_template('index.j2')

# Basic Var capture - GET on /hello/
@app.route("/hello/")
@app.route("/hello/<name>")
def home(name):
    return render_template('hello.j2',name=name)

# Testing out returning JSON from a URL
@app.route("/json")
def json_test():
  return json.dumps({"Test" : 50})


@app.get("/scan")
def scan_urls():
  scanner = network.SSL_Scanner("www.google.com", 443)
  details = scanner.get_certificate()
  return json.dumps(scanner.print_basic_info(details))














# ======================== SQL Tutorial Stuff =========================

@app.route('/widgets')
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

@app.route('/initdb')
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