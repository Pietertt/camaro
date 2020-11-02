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

@app.route("/activities/recent")
def helloWorld():
    cursor.execute("SELECT * FROM `activities` LIMIT 5")
    result = cursor.fetchall()

    results = []

    for x in result:
        results.append(x)

    return json.dumps(results)

@app.route("/activities/monthly")
def get_activities_monthly():
    cursor.execute("SELECT COUNT(SUBSTRING(activities.timestamp, 7, 2)) FROM activities GROUP BY SUBSTRING(activities.timestamp, 7, 2) ORDER BY COUNT(SUBSTRING(activities.timestamp, 7, 2)) DESC")
    result = cursor.fetchall()

    results = []

    for x in result:
        results.append(x[0])

    return json.dumps(results)