from flask import Flask
from flask import render_template
from flask import request
from flask import Blueprint
from .utils import network
from .utils import db_connector
from .data import Structs


# Define this python file as the blueprint 
certs = Blueprint('certs', __name__) # __name__ is essentially the main() of this python file

# Index of Certs
@certs.route("/")
def index():
  pagedata = Structs.PageData()

  # Run Query and get results
  db_conn = db_connector.MySQL_Connector()
  q_headers, q_results = db_conn.Run_Query("select * from certificates")

  # Render
  return render_template(
                          'certs_index.j2', 
                          pagedata=pagedata, 
                          sub_title="Certificates",
                          table_title="Discovered SSL Certificates",
                          headers=q_headers, 
                          results=q_results
                        )


