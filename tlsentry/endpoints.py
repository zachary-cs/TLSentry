from flask import Flask
from flask import render_template
from flask import request
from flask import Blueprint
from .utils import network
from .utils import db_connector
from .data import Structs


# Define this python file as the blueprint 
endpoints = Blueprint('endpoints', __name__) # __name__ is essentially the main() of this python file

# Index of endpoints
@endpoints.route("/")
def index():
  pagedata = Structs.PageData()
  
  # Run Query and get results
  db_conn = db_connector.MySQL_Connector()
  q_headers, q_results = db_conn.Run_Query("select * from endpoints")

  # Render
  return render_template(
                          'endpoints_index.j2', 
                          pagedata=pagedata, 
                          sub_title="Endpoints",
                          table_title="Node Endpoints",
                          headers=q_headers, 
                          results=q_results
                        )

