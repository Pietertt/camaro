from tensorflow import keras
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense
from keras.preprocessing.image import ImageDataGenerator
from keras.preprocessing import image
from keras.applications.vgg16 import preprocess_input
import numpy as np

from CustomModel import CustomModel

model = CustomModel()

model.define_model()
#model.train()
model.predict('data/validation/cats/cat.4030.jpg')