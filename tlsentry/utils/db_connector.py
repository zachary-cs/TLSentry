import mysql.connector
import json


class MySQL_Connector():


  def __init__(self):
    # Template for DB Connection
    self.mydb = mysql.connector.connect(
      host="mysqldb",
      user="root",
      password="p@ssw0rd1",
      database="inventory"
    )
  

  def Run_Query(string):      
    self.cursor = mydb.cursor()


    self.cursor.execute("SELECT * FROM widgets")

    row_headers=[x[0] for x in cursor.description] #this will extract row headers

    self.results = cursor.fetchall()
    self.json_data=[]
    for result in self.results:
      self.json_data.append(dict(zip(row_headers,result)))

    self.cursor.close()

    return json.dumps(self.json_data)
