import keras
import os
from keras import Sequential
from keras.layers import Dense
from keras.layers import Conv2D
from keras.layers import MaxPool2D
from keras.layers import Flatten


def save_model(model):
    if not os.path.exists('Data/Model'):
        os.makedirs('Data/Model')
    model_json = model.to_json()
    with open('Data/Model/model.json', 'w') as modelFile:
        modelFile.write(model_json)
    model.save_weights('Data/Model/weights.h5')
    print('Model and weights saved')
    return


def create_model():
    model = Sequential()
    model.add(Conv2D(filters=8, kernel_size=(3, 3), activation='relu', input_shape=(120, 160, 3)))
    model.add(Conv2D(filters=16, kernel_size=(3, 3), activation='relu'))
    model.add(MaxPool2D())
    model.add(Conv2D(filters=16, kernel_size=(3, 3), activation='relu'))
    model.add(Conv2D(filters=32, kernel_size=(3, 3), activation='relu'))
    model.add(Flatten())
    model.add(Dense(256, activation='relu'))
    model.add(Dense(128, activation='relu'))
    model.add(Dense(2, activation='softmax'))
    model.compile(optimizer='adam',
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])
    return model


if __name__ == '__main__':
    save_model(create_model())
