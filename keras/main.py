import json
import datetime
import time
from flask import Flask
from flask_cors import CORS

from CustomModel import CustomModel

app = Flask(__name__)
CORS(app)


@app.route("/network")
def helloWorld():
    model = CustomModel()
    model.define_model()
    return model.predict("data/validation/dogs/dog.4034.jpg")
