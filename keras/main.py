import json
import datetime
import time
from flask import Flask
from flask import request
from flask_cors import CORS

from CustomModel import CustomModel

# app = Flask(__name__)
# CORS(app)


# @app.route("/network/predict")
# def helloWorld():
model = CustomModel()
model.define_model()
model.train()
print(str(model.predict("data/validation/dogs/dog." + request.args.get('image') + ".jpg")))
