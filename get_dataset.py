import numpy as np
import cv2
import time
import os
from keras.utils import normalize
from keras.preprocessing.image import ImageDataGenerator

def getLabeledCaptures(amount, label):
    imgs = []
    labels = []
    for times in range(amount):
        cap = cv2.VideoCapture(0)
        if cap.isOpened():
            ret, frame = cap.read()
            img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = cv2.resize(img, (160, 120), interpolation=cv2.INTER_AREA)
            imgs.append(img)
            labels.append(label)
            cap.release()
            time.sleep(0.1)

    return normalize(np.array(imgs), axis=1), np.array(labels)


def getCapture():
    cap = cv2.VideoCapture(0)
    if cap.isOpened():
        ret, frame = cap.read()
        img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = cv2.resize(img, (160, 120), interpolation=cv2.INTER_AREA)

        cap.release()
        return normalize(np.array(img), axis=1)
    else:
        return getCapture()


def get_dataset(amountOfSample):
    global x_train
    global y_train
    if os.path.isfile('./Data/x_train.npy') and os.path.isfile('./Data/y_train.npy'):
        x_train = np.load('Data/x_train.npy')
        y_train = np.load('Data/y_train.npy')
        ImageDataGenerator(horizontal_flip=True, vertical_flip=False).fit(x_train)
        return x_train,y_train
    if not os.path.isfile('./Data/x_train1.npy'):
        skip = input('Hirsizlik dataseti olusturmak icin: Enter')
        x_train1, y_train1 = getLabeledCaptures(amountOfSample, 1)
        x_train1, y_train1 = np.array(x_train1), np.array(y_train1)
        np.save('Data/x_train1', x_train1)
        np.save('Data/y_train1', y_train1)
    else:
        x_train1 = np.load('Data/x_train1.npy')
        y_train1 = np.load('Data/y_train1.npy')
    skip = input('Guvenli alan taramasini baslatmak icin: Enter ')
    x_train0, y_train0 = getLabeledCaptures(30, 0)
    x_train0, y_train0 = np.array(x_train0), np.array(y_train0)
    for i in range (2,int(amountOfSample/30)+1):
        skip = input('tarama: ' + str(i)+'/' + str(int(amountOfSample/30)) +' baslatmak icin: Enter')
        x_train0temp , y_train0temp =  getLabeledCaptures(30, 0)
        x_train0temp , y_train0temp =  np.array(x_train0temp), np.array(y_train0temp)
        x_train0 = np.concatenate((x_train0, x_train0temp), axis=0)
        y_train0 = np.concatenate((y_train0, y_train0temp), axis=0)
    x_train = normalize(np.concatenate((x_train0, x_train1), axis=0), axis=1)
    y_train = np.concatenate((y_train0, y_train1), axis=0)
    np.save('Data/x_train.npy', x_train)
    np.save('Data/y_train.npy', y_train)
    y_train.reshape(len(y_train), 1)
    ImageDataGenerator(horizontal_flip=True, vertical_flip=False).fit(x_train)

    return x_train, y_train