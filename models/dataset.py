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

DATADIR = "/home/jason/projects/AntiJacker/hilbert"
CATEGORIES = ["benign", "malicious"]
X_IMG_SIZE = 32
Y_IMG_SIZE = 32

training_data = []

def create_training_data():
    for category in CATEGORIES:

        path = os.path.join(DATADIR,category)  # create path
        class_num = CATEGORIES.index(category)  # get the classification  (0 or a 1). 0=benign 1=malicious

        for img in tqdm(os.listdir(path)):
            try:
                img_array = cv2.imread(os.path.join(path,img) ,cv2.IMREAD_GRAYSCALE)  # convert to array
                new_array = cv2.resize(img_array, (X_IMG_SIZE, Y_IMG_SIZE))  # resize to normalize data size
                training_data.append([new_array, class_num])  # add this to our training_data
            except Exception as e:  # in the interest in keeping the output clean...
                pass
            #except OSError as e:
            #    print("OSErrroBad img most likely", e, os.path.join(path,img))
            #except Exception as e:
            #    print("general exception", e, os.path.join(path,img))
    print(len(training_data))

    random.shuffle(training_data)
    x = []
    y = []

    for sample in training_data[:30]:
    	print(sample[1])

    for features, label in training_data:
    	x.append(features)
    	y.append(label)

    x = np.array(x).reshape(-1, X_IMG_SIZE, Y_IMG_SIZE, 1)

    pickle_out = open("X.pickle", "wb")
    pickle.dump(x, pickle_out)
    pickle_out.close()

    pickle_out = open("Y.pickle", "wb")
    pickle.dump(y, pickle_out)
    pickle_out.close()

def load_training_data():
	if (os.path.exists("X.pickle") is False) or (os.path.exists("Y.pickle") is False):
		create_training_data()

	pickle_in = open("X.pickle","rb")
	X = pickle.load(pickle_in)

	pickle_in = open("Y.pickle","rb")
	Y = pickle.load(pickle_in)

	return X, Y
