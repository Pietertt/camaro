from tensorflow import keras
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense, BatchNormalization
from keras.preprocessing.image import ImageDataGenerator
from keras.preprocessing import image
from keras.applications.vgg16 import preprocess_input
from keras.utils import to_categorical
from sklearn.model_selection import train_test_split
import pandas
import numpy as np
import json
from keras.callbacks import EarlyStopping, ReduceLROnPlateau
import os

class CustomModel(keras.Model):
    image_width = 150
    image_height = 150
    image_channels = 3
    batch_size = 15


    model = None

    def __init__(self):
        super(CustomModel, self).__init__()

    def define(self) -> None:
        model = Sequential()
        model.add(Conv2D(32, (3,3), activation = 'relu', input_shape = (self.image_width, self.image_height, self.image_channels)))
        model.add(BatchNormalization())
        model.add(MaxPooling2D(pool_size = (2, 2)))
        model.add(Dropout(0.25))
        model.add(Conv2D(64, (3, 3), activation = 'relu'))
        model.add(BatchNormalization())
        model.add(MaxPooling2D(pool_size = (2, 2)))
        model.add(Dropout(0.25))
        model.add(Conv2D(150, (3, 3), activation = 'relu'))
        model.add(BatchNormalization())
        model.add(MaxPooling2D(pool_size = (2, 2)))
        model.add(Dropout(0.25))
        model.add(Flatten())
        model.add(Dense(512, activation = 'relu'))
        model.add(BatchNormalization())
        model.add(Dropout(0.5))
        model.add(Dense(2, activation = 'softmax'))
        model.compile(loss = 'categorical_crossentropy', optimizer = 'rmsprop', metrics = ['accuracy'])

        self.model = model
       
    def get_model(self) -> Sequential:
        return self.model

    def summary(self) -> None:
        self.model.summary()

    def prepare(self) -> None:
        filenames = os.listdir("./data/train")
        categories=[]
        for f_name in filenames:
            category = f_name.split('.')[0]
            if category == 'dog':
                categories.append(1)
            else:
                categories.append(0)
        self.df = pandas.DataFrame({
            'filename' : filenames,
            'category' : categories
        })

        self.earlystop = EarlyStopping(patience = 10)
        self.learning_rate_reduction = ReduceLROnPlateau(monitor = 'val_acc',patience = 2,verbose = 1,factor = 0.5,min_lr = 0.00001)
        self.callbacks = [self.earlystop, self.learning_rate_reduction]

        self.df["category"] = self.df["category"].replace({0: 'cat', 1: 'dog'})
        self.train_df, self.validate_df = train_test_split(self.df, test_size = 0.20, random_state=42)
        self.train_df = self.train_df.reset_index(drop = True)
        self.validate_df = self.validate_df.reset_index(drop = True)
        self.total_train = self.train_df.shape[0]
        self.total_validate = self.validate_df.shape[0]
        

        self.train_datagen = ImageDataGenerator(rotation_range = 15, rescale = 1. / 255, shear_range = 0.1, zoom_range = 0.2, horizontal_flip = True, width_shift_range = 0.1, height_shift_range = 0.1)
        self.train_generator = self.train_datagen.flow_from_dataframe(self.train_df, "./data/train/", x_col = 'filename', y_col = 'category', target_size = (self.image_width, self.image_height), class_mode = 'categorical', batch_size = self.batch_size)
        self.validation_datagen = ImageDataGenerator(rescale = 1. / 255)
        self.validation_generator = self.validation_datagen.flow_from_dataframe(self.validate_df, "./data/validation/",  x_col='filename', y_col='category', target_size = (self.image_width, self.image_height), class_mode = 'categorical', batch_size = self.batch_size)
    
    def train(self) -> None:
        epochs=10
        history = self.model.fit_generator(
            self.train_generator, 
            epochs=epochs,
            validation_data=self.validation_generator,
            validation_steps=self.total_validate//self.batch_size,
            steps_per_epoch=self.total_train//self.batch_size,
            callbacks=self.callbacks
        )

        self.model.save("testenen.h5")

    #     batch_size = 16

    #     train_datagen = ImageDataGenerator(rescale=1./255, shear_range=0.2, zoom_range=0.2, horizontal_flip=True)
    #     self.train_generator = train_datagen.flow_from_directory('data/train', target_size=(150, 150), batch_size=16, class_mode='binary') 

    #     test_datagen = ImageDataGenerator(rescale=1./255)


    #     self.validation_generator = test_datagen.flow_from_directory('data/validation', target_size=(150, 150), batch_size=batch_size, class_mode='binary')

    #     self.model = model

    # def train(self):
    #     #self.model.fit_generator(self.train_generator, steps_per_epoch=200, epochs=20, validation_data=self.validation_generator, validation_steps=800)
    #     history = self.model.fit_generator(self.train_generator, epochs=10, validation_data=self.validation_generator, validation_steps=total_validate//16, steps_per_epoch=total_train//16)
    #     self.model.save('catndogs1')  # always save your weights after training or during training 

    # def predict(self, file):
    #     model = keras.models.load_model("catndogs")
        
    #     try:
    #         img = image.load_img(file, target_size=(150, 150))
    #     except FileNotFoundError:
    #         return "File not found"
    #     x = image.img_to_array(img)
    #     x = np.expand_dims(x, axis=0)
    #     x = preprocess_input(x)

    #     preds = model.predict(x)

    #     self.train_generator.class_indices

    #     return preds