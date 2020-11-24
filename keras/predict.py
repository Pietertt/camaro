from tensorflow import keras
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense
from keras.preprocessing.image import ImageDataGenerator
from keras.preprocessing import image
from keras.applications.vgg16 import preprocess_input
import numpy as np

model = keras.models.load_model("my_model")

# The local path to our target image
img_path = 'data/validation/dogs/dog.4001.jpg'
# `img` is a PIL image of size 224x224
img = image.load_img(img_path, target_size=(150, 150))
# `x` is a float32 Numpy array of shape (224, 224, 3)
x = image.img_to_array(img)
# We add a dimension to transform our array into a "batch"
# of size (1, 224, 224, 3)
x = np.expand_dims(x, axis=0)
# Finally we preprocess the batch
# (this does channel-wise color normalization)
x = preprocess_input(x)
preds = model.predict(x)
train_generator.class_indices
if preds[0][0] == 1:
    prediction = 'dog'
else:
    prediction = 'cat'

print(preds)

print(prediction)