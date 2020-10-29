import mysql.connector
import json
import datetime

from flask import Flask

database = mysql.connector.connect(
  host="mysql",
  user="root",
  password="root",
  database="camaro",
  port="3306"
)

cursor = database.cursor()

app = Flask(__name__)

@app.route('/')
def hello():
    cursor.execute("SELECT * FROM `activities`")
    myresult = cursor.fetchall()

    return json.dumps(myresult)
