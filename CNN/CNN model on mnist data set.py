#import tensorflow as tf
import cv2
from keras.datasets import mnist
from keras.utils import to_categorical
from keras.layers import Convolution2D , MaxPooling2D, Activation, Flatten, Dense
from keras.models import Sequential
import matplotlib.pyplot as plt
import numpy as np






(x_train , y_train) , (x_test , y_test) = mnist.load_data()
print(x_train.shape)


x_train = x_train.reshape(x_train.shape[0],28,28,1)
x_test = x_test.reshape(x_test.shape[0],28,28,1)

x_train = x_train.astype("float32")
x_test = x_test.astype("float32")

x_train /= 255 - 0.5
x_test /= 255 - 0.5







model = Sequential()
model.add(Convolution2D(6, 3, activation='relu', input_shape=x_train.shape[1:]))
model.add(MaxPooling2D(pool_size = 2))
#model.add(Convolution2D(1, 10, activation='relu'))
model.add(Flatten())
model.add(Dense(10, activation="softmax"))

model1.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])


model1.fit(x_train, to_categorical(y_train), verbose = 2 ,validation_data=(x_test, to_categorical(y_test)), epochs=3)


####model1.add(Convolution2D(filters, filter size, activation='relu', input_shape=image.shape)
##
##
##
##conv_img = model1.predict(img)




##model = Sequential()
###add model layers
##model.add(Conv2D(64, kernel_size=3, activation="relu", input_shape=(28,28,1)))
##model.add(Conv2D(32, kernel_size=3, activation="relu"))
##model.add(Flatten())
##model.add(Dense(10, activation=’softmax’))
##
##
##







############image = cv2.imread("sheen.png",cv2.IMREAD_GRAYSCALE)
############print(image.shape)
############
############_ , image = cv2.threshold(image,127,255,cv2.THRESH_BINARY)
############
############print(image)
############plt.imshow(image)
############plt.show()

