import argparse,os

parser=argparse.ArgumentParser()
parser.add_argument("gpu",type=int)
args=parser.parse_args()

gpu=args.gpu
assert gpu>=0 and gpu<4

os.environ["CUDA_VISIBLE_DEVICES"]=str(gpu)

import tensorflow as tf
from tensorflow.keras import layers
import numpy as np

model = tf.keras.Sequential()
# Adds a densely-connected layer with 64 units to the model:
model.add(layers.Dense(64, activation='relu'))
# Add another:
model.add(layers.Dense(64, activation='relu'))
# Add a softmax layer with 10 output units:
model.add(layers.Dense(10, activation='softmax'))

model.compile(optimizer=tf.train.AdamOptimizer(0.001),
    loss='mse', metrics=['accuracy'])

data = np.random.random((1000, 32))
labels = np.random.random((1000, 10))

model.fit(data, labels, epochs=1000, batch_size=32)
