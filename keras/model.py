from tensorflow import keras
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense
from keras.preprocessing.image import ImageDataGenerator
from keras.preprocessing import image
from keras.applications.vgg16 import preprocess_input
import numpy as np

model = Sequential()
model.add(Conv2D(32, (3, 3), input_shape=(150, 150, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(32, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(64, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Flatten())  # this converts our 3D feature maps to 1D feature vectors
model.add(Dense(64))
model.add(Activation('relu'))
model.add(Dropout(0.5))
model.add(Dense(1))
model.add(Activation('sigmoid'))

model.compile(loss='binary_crossentropy',
              optimizer='rmsprop',
              metrics=['accuracy'])

batch_size = 16

# this is the augmentation configuration we will use for training
train_datagen = ImageDataGenerator(
        rescale=1./255,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True)

# this is the augmentation configuration we will use for testing:
# only rescaling
test_datagen = ImageDataGenerator(rescale=1./255)

# this is a generator that will read pictures found in
# subfolers of 'data/train', and indefinitely generate
# batches of augmented image data
train_generator = train_datagen.flow_from_directory(
        'data/train',  # this is the target directory
        target_size=(150, 150),  # all images will be resized to 150x150
        batch_size=batch_size,
        class_mode='binary')  # since we use binary_crossentropy loss, we need binary labels

# this is a similar generator, for validation data
validation_generator = test_datagen.flow_from_directory(
        'data/validation',
        target_size=(150, 150),
        batch_size=batch_size,
        class_mode='binary')

# model.fit_generator(
#         train_generator,
#         steps_per_epoch=200 // batch_size,
#         epochs=10,
#         validation_data=validation_generator,
#         validation_steps=800 // batch_size)
#model.save('my_model')  # always save your weights after training or during training


# # The local path to our target image
# img_path = '/Users/pieterboersma/desktop/dog.jpg'
# # `img` is a PIL image of size 224x224
# img = image.load_img(img_path, target_size=(150, 150))
# # `x` is a float32 Numpy array of shape (224, 224, 3)
# x = image.img_to_array(img)
# # We add a dimension to transform our array into a "batch"
# # of size (1, 224, 224, 3)
# x = np.expand_dims(x, axis=0)
# # Finally we preprocess the batch
# # (this does channel-wise color normalization)
# x = preprocess_input(x)
# preds = model.predict(x)
# train_generator.class_indices
# if preds[0][0] == 1:
#     prediction = 'dog'
# else:
#     prediction = 'cat'

# print(preds)

# print(prediction)

model = keras.models.load_model("my_model")

# The local path to our target image
img_path = 'data/validation/dogs/dog.4006.jpg'
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