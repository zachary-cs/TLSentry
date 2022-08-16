from flask import Flask
from flask import render_template
from flask import request
from flask import Blueprint
from cryptography.hazmat.primitives import hashes
import datetime
from .utils import network
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


# New endpoint form page
@endpoints.route("/add", methods=['GET','POST'])
def add():
  pagedata = Structs.PageData()
  # Posted form from /add page
  if request.method == 'POST':
    # TODO
    hostname = request.form['hostname']
    port = request.form['port']

    # Port Checking
    if port == '':
      port = 443
    else:
      port = int(port)

    # Create the Scanner and obtain the SSL Certificate
    scanner = network.Scanner(hostname, port)
    cert = scanner.Certificate
    return scanner.Crypto_Cert.toStr()


    if cert is None:
      return "Certificate not found!"

    # Gather details for Endpoint
    Peer_Name = cert.GetDict()['Peer Name'][0]

    Datetime_Now = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")

    # Open DB Connection
    db_conn = db_connector.MySQL_Connector()

    # Check if the Certificate Exists
    q_headers, q_results = db_conn.Run_Query(f"select * from certificates where common_name = '{cert.Hostname}'")

    if len(q_results) >= 1:
      # Cert already in store, get it's id
      cert_id = q_results[0]["id"]
    else:
      # Certificate does not exist, insert it and get the ID
      query = f"INSERT INTO tlsentry.certificates \
                (common_name, peer_name, alt_names, issuer, not_before, not_after, thumbprint) \
                VALUES \
                ('{cert.CommonName}', '{Peer_Name}', 'None', '{cert.Issuer}', '{cert.NotBefore}', '{cert.NotAfter}', 'TEESDFSKLJDFhKLSDJgfsajdf');"
      q_headers, q_results = db_conn.Run_Query(query)

    
    # Return Test Page - DEBUGGING
    return f"Submitted, <br><br> request method = {request.method},<br><br> form data = {request.form}, <br><br> cert = {cert.GetDict()},<br><br> cert_db = {q_results}, <br><br> Peer IP =  "

    # Create the Endpoint record
    q_headers, q_results = db_conn.Run_Query(f"insert into endpoints values ( {hostname},{cert.PeerName[0]},{port},NULL )")

    # Return user to endpoints index, and highlight the new endpoint
    return render_template(
                            'endpoints_index.j2', 
                            pagedata=pagedata, 
                            sub_title="Add an Endpoint"
                          ) 
  elif request.method == 'GET':
  
    # Render
    return render_template(
                            'endpoints_add.j2', 
                            pagedata=pagedata, 
                            sub_title="Add an Endpoint"
                          )
