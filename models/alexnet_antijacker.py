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

	x_data = x_data/255.0

	x_data = np.array(x_data)
	y_data = np.array(y_data)

	x_val = x_data[-340:,:,:,:]
	y_val = y_data[-340:]
	x_train = x_data[:-340,:,:,:]
	y_train = y_data[:-340]
	print(len(x_train))

	print(x_data.shape)
	print(y_data.shape)

	model = models.Sequential()
	model.add(layers.experimental.preprocessing.Resizing(224, 224, interpolation="bilinear", input_shape=x_train.shape[1:]))
	model.add(layers.Conv2D(96, 11, strides=4, padding='same'))
	model.add(layers.Lambda(tf.nn.local_response_normalization))
	model.add(layers.Activation('relu'))
	model.add(layers.MaxPooling2D(3, strides=2))
	model.add(layers.Conv2D(256, 5, strides=4, padding='same'))
	model.add(layers.Lambda(tf.nn.local_response_normalization))
	model.add(layers.Activation('relu'))
	model.add(layers.MaxPooling2D(3, strides=2))
	model.add(layers.Conv2D(384, 3, strides=4, padding='same'))
	model.add(layers.Activation('relu'))
	model.add(layers.Conv2D(384, 3, strides=4, padding='same'))
	model.add(layers.Activation('relu'))
	model.add(layers.Conv2D(256, 3, strides=4, padding='same'))
	model.add(layers.Activation('relu'))
	model.add(layers.Flatten())
	model.add(layers.Dense(4096, activation='relu'))
	model.add(layers.Dropout(0.5))
	model.add(layers.Dense(4096, activation='relu'))
	model.add(layers.Dropout(0.5))
	model.add(layers.Dense(1, activation='sigmoid'))
	model.summary()

	model.compile(optimizer=tf.keras.optimizers.Adam(lr=1e-5), loss=tf.keras.losses.BinaryCrossentropy(), metrics=['accuracy'])

	weights = {0: 2.89,
			   1: 0.6}

	history = model.fit(x_train, y_train, batch_size=8, epochs=16, validation_data=(x_val, y_val), class_weight=weights)

	fig, axs = plt.subplots(2, 1, figsize=(15,15))

	axs[0].plot(history.history['loss'])
	axs[0].plot(history.history['val_loss'])
	axs[0].title.set_text('Training Loss vs Validation Loss')
	axs[0].legend(['Train', 'Val'])

	axs[1].plot(history.history['accuracy'])
	axs[1].plot(history.history['val_accuracy'])
	axs[1].title.set_text('Training Accuracy vs Validation Accuracy')
	axs[1].legend(['Train', 'Val'])
	plt.show()


if __name__ == "__main__":
	main()
