#This is 'Asuka' the 'McNuts' model pilot from ouroboros

import numpy as np
import matplotlib.pyplot as plt
from pandas import read_csv
import pandas as pd
import math
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error
from keras.models import model_from_json
from keras.models import load_model

from keras.layers import Dropout, Activation
from keras.optimizers import SGD
from keras.layers.recurrent import LSTM
from keras.layers.convolutional import Convolution2D

print('"Asuka" the "McNuts" model pilot from ouroboros')

print('Loading model: McNuts')

model = load_model(r'C:\Users\Usuario\Documents\GitHub\Leviathan\Leviathan\Fortune Tellers\Models\Eva.h5')

print('model loaded')


Location = r'C:\Users\Usuario\Documents\GitHub\Leviathan\Leviathan\Pilots\predictionsample.csv'
sample = pd.read_csv(Location)

sample = np.array([sample.date])

print('Making predictions')

predictions = model.predict(sample)