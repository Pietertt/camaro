import mysql.connector
import json
import datetime

from models.Activity import Activity

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

@app.route("/activities/valid/all")
def get_all_valid_activities():
    cursor.execute("SELECT COUNT(activities.valid) FROM activities WHERE activities.valid = 1")
    result = cursor.fetchall()

    return json.dumps(result)

@app.route("/activities/invalid/all")
def get_all_invalid_activities():
    cursor.execute("SELECT COUNT(activities.valid) FROM activities WHERE activities.valid = 0")
    result = cursor.fetchall()

    return json.dumps(result)

@app.route("/activities/delete/all")
def delete_all_activities():
    cursor.execute("DELETE FROM activities")
    database.commit()

    return str(200)

@app.route("/sensor/delete/all")
def delete_all_sensor():
    cursor.execute("DELETE FROM sensor_values")
    database.commit()

    return str(200)

@app.route("/activities/monthly")
def get_activities_monthly():
    cursor.execute("SELECT DATE(activities.timestamp), COUNT(activities.timestamp) AS TOT FROM activities GROUP BY DATE(activities.timestamp)")
    result = cursor.fetchall()

    results = []

    for x in result:
        activity = Activity(1)
        activity.set_day(str(x[0])[8:10])

        subarray = []
        subarray.append(x[1])
        subarray.append(str(activity.get_day()))

        results.append(subarray)

    return json.dumps(results)