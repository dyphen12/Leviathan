#Basic Deep Learning Neural Network "EVA_Prototype"

#The first functional EVA for Leviathan

'This prototype is for a univariate dataset'
'This EVA only predicts the basic BTC/USD Chart'

import plotly as py
import plotly.graph_objs as go
import pandas as pd
import numpy as np
from matplotlib.pyplot import subplots, draw
from sklearn.preprocessing import MinMaxScaler
from sklearn import preprocessing
from sklearn.preprocessing import LabelEncoder


from sklearn.model_selection import train_test_split


print("EVA_Prototype")
print("")
print("Initializing...")
print("")
print("EVA_Prototype // ON")

#Analyze of the dataset
print("Getting dataset // NOW USING: pandas")

Location = r'C:\Users\Usuario\Documents\GitHub\Leviathan\Leviathan\Fortune Tellers\Datasets\Eva prototype\BTCUSD_Coindesk.csv'
df = pd.read_csv(Location)

print("Dataset loaded!")

print("Splitting the data")

train_labels=np.array(df.date)
#Train_Samples ohlc
#train_samples=np.array([df.open,df.high,df.low,df.close])
train_samples=np.array(df.close)


print("Data successfully splitted!")
print("")
print("")
print("PREPROCESSING DATA FOR: Multilayer Perceptron")
print("")
print("STARTING...")

'This is how we process the data for a multilayer perceptron'
scaler = MinMaxScaler(feature_range=(0, 1))
#scaled_train_samples = scaler.fit_transform(train_samples)
'That s it!'

print("DATA PROCESSED")
print("")
print("EVA_prototype // STARTING BUILDING NN")

#Keras Imports

import keras
from keras.models import Sequential
from keras.layers import Activation
from keras.layers.core import Dense
from keras.optimizers import Adam
from keras.metrics import categorical_crossentropy


model = Sequential([
    Dense(8,input_shape=(1,),activation='relu'),
    Dense(6,activation='relu'),
    Dense(1, activation='softmax')
])

print("EVA_prototype // NN BUILD")
print("")
print("EVA_prototype // THIS IS EVA")
model.summary()
print("EVA_prototype // COMPILING EVA ")

model.compile(Adam(lr=(0.001)),loss='sparse_categorical_crossentropy',metrics=['accuracy'])

print("EVA_prototype // COMPILED SUCCESSFULLY ")
print("")
print("EVA_prototype // TRAINING EVA")
model.fit(train_samples,train_labels,batch_size=10,epochs=200,shuffle=True,verbose=1)