import mysql.connector
import json
import datetime
import numpy
import tensorflow
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.vgg16 import preprocess_input
from PIL import Image
import os

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
from flask import request

app = Flask(__name__)
CORS(app)


@app.route("/activities/recent")
def helloWorld():
    userid = request.args.get('userid')
    cursor.execute("SELECT * FROM `activities` WHERE valid = 1 AND userid=" + userid + " ORDER BY id DESC LIMIT 5")
    result = cursor.fetchall()

    results = []

    for x in result:
        results.append(x)

    return json.dumps(results)


@app.route("/activities/all")
def get_all_activities():
    userid = request.args.get('userid')
    cursor.execute("SELECT * FROM `activities` WHERE valid = 1 AND userid=" + userid + " ORDER BY timestamp DESC")
    result = cursor.fetchall()

    return json.dumps(result)



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


@app.route("/activities/monthly")
def get_activities_monthly():
    userid = request.args.get('userid')
    cursor.execute("SELECT DATE(activities.timestamp), COUNT(activities.timestamp) AS TOT FROM activities WHERE userid=" + userid + " GROUP BY DATE(activities.timestamp) ORDER BY DATE(activities.timestamp) ASC")
    result = cursor.fetchall()

    results = []

    for x in result:
        activity = Activity(1)
        activity.set_day(int(str(x[0])[8:10]))

        subarray = []
        subarray.append(x[1])
        subarray.append(activity.get_day())

        results.append(subarray)

    return json.dumps(results)


@app.route("/activities/delete/all")
def delete_all_activities():
    cursor.execute("DELETE FROM activities")
    database.commit()

    return str(200)


@app.route("/activities/percentage")
def get_activities_percentage():
    userid = request.args.get('userid')
    cursor.execute("SELECT COUNT(activities.valid) FROM activities WHERE userid = " + userid + " AND valid = 1")
    valid = cursor.fetchall()

    cursor.execute("SELECT COUNT(activities.valid) FROM activities WHERE userid = " + userid + " AND valid = 0")
    invalid = cursor.fetchall()
    
    if (str(valid[0])[1] == '0' and str(invalid[0])[1] == '0'):
        data = []
        data.append(0)
        data.append(0)
        return json.dumps(data)

    if str(invalid[0])[1] == '0':
        data = []
        data.append(100)
        data.append(0)
        return json.dumps(data)

    if str(valid[0])[1] == '0':
        data = []
        data.append(0)
        data.append(100)
        return json.dumps(data)

    valid = valid[0][0]
    invalid = invalid[0][0]

    total = valid + invalid

    data = []
    data.append(int((valid / total) * 100))
    data.append(int((invalid / total) * 100))

    return (json.dumps(data))

@app.route("/sensor/value/recent")
def get_values():
    userid = request.args.get('userid')
    cursor.execute("SELECT sensor_values.distance, sensor_values.ldr FROM `sensor_values` WHERE userid = " + userid + " ORDER BY sensor_values.ID DESC LIMIT 1")
    value = cursor.fetchall()

    return json.dumps(value) 


@app.route("/sensor/delete/all")
def delete_all_sensor():
    cursor.execute("DELETE FROM sensor_values")
    database.commit()

    return str(200)

@app.route("/image/validate")
def validate_image():
    model = tensorflow.keras.models.load_model("humansnfaces")

    img = image.load_img('images/' + str(request.args.get('image')), target_size=(128, 128))
    x = image.img_to_array(img)
    x = numpy.expand_dims(x, axis=0)
    x = preprocess_input(x)

    predict = model.predict(x)

    return str(round(predict[0][0], 2))