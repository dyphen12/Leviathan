#Eva the recurrent fortune teller of the btc-usd change


import pandas as pd
import numpy as np
import plotly as py
from sklearn.preprocessing import MinMaxScaler

from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.layers.recurrent import LSTM
import plotly.graph_objs as go

Location = r'C:\Users\Usuario\Documents\GitHub\Leviathan\Leviathan\Fortune Tellers\Datasets\Eva knowledge\btc-usd.csv'
df = pd.read_csv(Location)


trace = go.Candlestick(x=df.index,
                       open=df.open,
                       high=df.high,
                       low=df.low,
                       close=df.close)
data = [trace]
#py.offline.plot(data, filename='simple_candlestick.html')

print(df)


#Setting the dataset

train_labels=np.array([df.Date])
train_samples=np.array([df.open,df.high,df.low,df.close])

scaler = MinMaxScaler(feature_range=(0, 1))
scaled_train_samples= scaler.fit_transform((train_samples))



#Building the NN

print('Building NN')

model = Sequential()
model.add(Dense(32, input_shape=train_samples.shape[1:]))

model.add(Activation('relu'))
model.add(Activation('softmax'))
model.add(Dense(1))

print ('NN Build')

model.compile(optimizer='SGD',
              loss='binary_crossentropy',
              metrics=['accuracy'])

print ('NN Compiled')

model.fit(scaled_train_samples,train_labels, batch_size=10,epochs=200,shuffle=True)