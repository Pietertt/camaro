import tensorflow
import matplotlib.pyplot as plt
import sklearn
import pandas
import numpy
import json
import os
import PIL
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Activation
from tensorflow.keras.layers.experimental.preprocessing import Rescaling
from PIL import Image
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.vgg16 import preprocess_input
from datetime import datetime
from sklearn.model_selection import train_test_split

class CustomModel(tensorflow.keras.Model):
    image_width = 150
    image_height = 150
    image_channels = 3
    batch_size = 15

    model = None

    def __init__(self):
        super(CustomModel, self).__init__()

    def predict(self):
        self.model = tensorflow.keras.models.load_model("humansnfaces")

        img = image.load_img('humans/validation/yes/00050.png', target_size=(128, 128))
        x = image.img_to_array(img)
        x = numpy.expand_dims(x, axis=0)
        x = preprocess_input(x)

        predict = self.model.predict(x)

        print(round(predict[0][0], 2))