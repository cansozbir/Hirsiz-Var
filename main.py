import keras
import train
from get_dataset import getCapture
import time
import numpy as np
import pygame


def programLoop ():
    play = False
    model = train.getAnExistModel()
    while True:
        img = getCapture()
        img = keras.utils.normalize(img, axis=1)
        img = img.reshape(1, 120, 160, 3)
        Y = model.predict(img)
        if np.argmax(Y[0]) == 1:
            print('THIEF DETECTED')
            pygame.mixer.init()
            pygame.mixer.music.load('Data/alarm.wav')
            pygame.mixer.music.play()
            time.sleep(30)
        else:
            print('EVERYTHING IS OK!')
        time.sleep(0.75)

if __name__ == '__main__':
    programLoop()
