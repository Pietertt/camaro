#from flask import Flask
#from flask_cors import CORS

from CustomModel import CustomModel

#app = Flask(__name__)
#CORS(app)


# @app.route("/")
# def predict():

model = CustomModel()
model.define_model()
#model.train()
print(model.predict('data/pp-3.jpg'))
