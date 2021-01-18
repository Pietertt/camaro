from tensorflow import keras

class CustomCallback(keras.callbacks.Callback):
    
    def on_train_begin(self):
        print("Starting training on this.date")
