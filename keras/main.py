

from CustomModel import CustomModel

# app = Flask(__name__)
# CORS(app)


# @app.route("/network/predict")
# def helloWorld():
model = CustomModel()
model.define()
#model.summary()
model.prepare()
model.train()
#model.predict()

# model.define_model()
# model.train()
# print(str(model.predict("data/validation/dogs/dog." + request.args.get('image') + ".jpg")))
