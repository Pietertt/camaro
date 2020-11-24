from flask import Flask
from flask_cors import CORS

from CustomModel import CustomModel

app = Flask(__name__)
CORS(app)


@app.route("/")
def predict():
    model = CustomModel()
    model.define_model()
    return model.predict('data/validation/cats/cat.4030.jpg')
