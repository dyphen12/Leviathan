#Eva the recurrent fortune teller of the btc-usd change


import pandas as pd

import plotly as py

from keras.models import Sequential
from keras.layers import Dense, Activation

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

#Building the NN

print('Building NN')

model = Sequential()
model.add(Dense(32, input_dim=5))
model.add(Activation('relu'))
model.add(Activation('softmax'))
model.add(Dense(1))


print ('NN Build')

model.compile(optimizer='rmsprop',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

print ('NN Compiled')
