import mysql.connector
import json
import datetime

database = mysql.connector.connect(
  host="mysql",
  user="root",
  password="root",
  database="camaro",
  port="3306"
)

cursor = database.cursor()

from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def helloWorld():
    cursor.execute("SELECT * FROM `activities`")
    result = cursor.fetchall()

    results = []

    for x in result:
        results.append(x)

    return json.dumps(results)