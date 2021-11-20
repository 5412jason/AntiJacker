import tensorflow as tf
import matplotlib.pyplot as plt
from tensorflow.keras import datasets, layers, models, losses
import numpy as np
import matplotlib.pyplot as plt
import os
import cv2
from tqdm import tqdm
import random
import pickle
import tensorflow as tf
from tensorflow.keras import datasets, layers, models, losses
import dataset as data

def main():
	x_data, y_data = data.load_training_data()

	x_data = tf.pad(x_data, [[0, 0], [2,2], [2,2]])/255
	print(x_data.shape)

	x_data = tf.expand_dims(x_data, axis=3, name=None)
	print(x_data.shape)


	model = models.Sequential()
	model.add(layers.Conv2D(6, 5, activation='tanh', input_shape=x.shape[1:]))
	model.add(layers.AveragePooling2D(2))
	model.add(layers.Activation('sigmoid'))
	model.add(layers.Conv2D(16, 5, activation='tanh'))
	model.add(layers.AveragePooling2D(2))
	model.add(layers.Activation('sigmoid'))
	model.add(layers.Conv2D(120, 5, activation='tanh'))
	model.add(layers.Flatten())
	model.add(layers.Dense(84, activation='tanh'))
	model.add(layers.Dense(10, activation='softmax'))
	model.summary()

	model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

	history = model.fit(x_data, y_data, batchsize=32, epochs=40, validation_split=0.2)

	fig, axs = plt.subplots(2, 1, figsize=(15,15))

	axs[0].plot(history.history['loss'])
	axs[0].plot(history.history['val_loss'])
	axs[0].title.set_text('Training Loss vs Validation Loss')
	axs[0].legend(['Train', 'Val'])

	axs[1].plot(history.history['accuracy'])
	axs[1].plot(history.history['val_accuracy'])
	axs[1].title.set_text('Training Accuracy vs Validation Accuracy')
	axs[1].legend(['Train', 'Val'])
