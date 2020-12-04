from tensorflow import keras
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense, BatchNormalization
from keras.preprocessing.image import ImageDataGenerator
from keras.preprocessing import image
from keras.applications.vgg16 import preprocess_input
import numpy as np
import json

class CustomModel(keras.Model):
    def __init__(self):
        super(CustomModel, self).__init__()

    def define_model(self):
        model=Sequential()
        model.add(Conv2D(32,(3,3),activation='relu',input_shape=(150, 150, 3)))
        model.add(BatchNormalization())
        model.add(MaxPooling2D(pool_size=(2,2)))
        model.add(Dropout(0.25))
        model.add(Conv2D(64,(3,3),activation='relu'))
        model.add(BatchNormalization())
        model.add(MaxPooling2D(pool_size=(2,2)))
        model.add(Dropout(0.25))
        model.add(Conv2D(128,(3,3),activation='relu'))
        model.add(BatchNormalization())
        model.add(MaxPooling2D(pool_size=(2,2)))
        model.add(Dropout(0.25))
        model.add(Flatten())
        model.add(Dense(512,activation='relu'))
        model.add(BatchNormalization())
        model.add(Dropout(0.5))
        model.add(Dense(2,activation='softmax'))
        model.compile(loss='categorical_crossentropy',
        optimizer='rmsprop',metrics=['accuracy'])

        batch_size = 16

        train_datagen = ImageDataGenerator(rescale=1./255, shear_range=0.2, zoom_range=0.2, horizontal_flip=True)
        self.train_generator = train_datagen.flow_from_directory('data/train', target_size=(150, 150), batch_size=16, class_mode='binary') 

        test_datagen = ImageDataGenerator(rescale=1./255)


        self.validation_generator = test_datagen.flow_from_directory('data/validation', target_size=(150, 150), batch_size=batch_size, class_mode='binary')

        self.model = model

    def train(self):
        #self.model.fit_generator(self.train_generator, steps_per_epoch=200, epochs=20, validation_data=self.validation_generator, validation_steps=800)
        history = self.model.fit_generator(self.train_generator, epochs=10, validation_data=self.validation_generator, validation_steps=total_validate//16, steps_per_epoch=total_train//16)
        self.model.save('catndogs1')  # always save your weights after training or during training 

    def predict(self, file):
        model = keras.models.load_model("catndogs")
        
        try:
            img = image.load_img(file, target_size=(150, 150))
        except FileNotFoundError:
            return "File not found"
        x = image.img_to_array(img)
        x = np.expand_dims(x, axis=0)
        x = preprocess_input(x)

        preds = model.predict(x)

        self.train_generator.class_indices

        return preds