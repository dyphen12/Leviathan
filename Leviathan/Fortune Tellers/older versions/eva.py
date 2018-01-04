#Eva the recurrent fortune teller of the btc-usd change


import pandas as pd
import numpy as np
import plotly as py
from sklearn.preprocessing import MinMaxScaler

from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.layers import Permute

from keras.layers import RNN
from keras.layers import SimpleRNNCell
from keras.metrics import binary_crossentropy
from keras.optimizers import SGD
from keras.activations import softmax
from keras.activations import relu
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

dataset=train_samples

scaler = MinMaxScaler(feature_range=(0, 1))
scaled_train_samples = scaler.fit_transform(train_samples)

dataset = scaler.fit_transform(dataset)

train_size = int(len(dataset) * 0.67)
test_size = len(dataset) - train_size
train, test = dataset[0:train_size,:], dataset[train_size:len(dataset),:]
print(len(train), len(test))


def create_dataset(dataset, look_back=1):
	dataX, dataY = [], []
	for i in range(len(dataset)-look_back-1):
		a = dataset[i:(i+look_back), 0]
		dataX.append(a)
		dataY.append(dataset[i + look_back, 0])
	return np.array(dataX), np.array(dataY)

# reshape into X=t and Y=t+1
look_back = 1
trainX, trainY = create_dataset(train, look_back)
testX, testY = create_dataset(test, look_back)



trainX = np.reshape(train_samples, train_labels, train_samples)
trainX = np.reshape(train_samples, train_labels, train_samples)



#Building the NN

print('Building NN')

print('cell build')
model = Sequential()
model.add(LSTM())
model.add(Activation('softmax'))
model.add(Dense(1708))


print ('NN Build')

model.compile(optimizer='SGD',
              loss='binary_crossentropy',
              metrics=['accuracy'])

print ('NN Compiled')

model.fit(scaled_train_samples,train_labels, batch_size=10,epochs=200,shuffle=True)