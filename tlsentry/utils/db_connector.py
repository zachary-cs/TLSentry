import mysql.connector
import json


class MySQL_Connector():


  def __init__(self):
    # Template for DB Connection
    self.mydb = mysql.connector.connect(
      host="mysqldb",
      user="root",
      password="p@ssw0rd1",
      database="tlsentry"
    )
  

  def Run_Query(self, string):      
    self.cursor = self.mydb.cursor()

    # Run the SQL passed into this function
    self.cursor.execute(string)

    row_headers=[x[0] for x in self.cursor.description] #this will extract row headers

    self.results = self.cursor.fetchall()
    self.json_data=[]
    for result in self.results:
      self.json_data.append(dict(zip(row_headers,result)))

    self.cursor.close()

    return row_headers, json.dumps(self.json_data, default=str)
