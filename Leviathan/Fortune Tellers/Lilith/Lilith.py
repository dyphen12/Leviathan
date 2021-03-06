#Deep Learning Neural Network "EVA"

#The third functional EVA for Leviathan

'This prototype is for a Multivariate dataset'
'This EVA only predicts the basic BTC/USD Chart'
#data getting imports
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math

#Data preprocess imports
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error

# fix random seed for reproducibility
np.random.seed(7)

print("EVA_Prototype3")
print("")
print("Initializing...")
print("")
print("EVA_Prototype3 // ON")
print("")

# DATASETTING PROCESS
print("EVA_Prototype3 // DATASETTING PROCESS STARTED")
#Analyze of the dataset
print("Getting dataset // NOW USING: pandas")

Location = r'C:\Users\Usuario\Documents\GitHub\Leviathan\Leviathan\Fortune Tellers\Datasets\Eva prototype\BTCUSD_Coindesk.csv'
dataframe = pd.read_csv(Location,usecols=[1], engine='python', skipfooter=1)

dataset = dataframe.values
dataset = dataset.astype('float32')

print("Dataset loaded!")
print("")
'Note: The dataset needs to be plotted by matplotlib, if is plotted then works.'

import matplotlib.pyplot as plt

print("Plotting dataset")
plt.plot(dataset)
plt.show()
print("Dataset plotted")
print("")
# normalize the dataset
print("Normalizing dataset...")
scaler = MinMaxScaler(feature_range=(0, 1))
dataset = scaler.fit_transform(dataset)

# split into train and test sets

#Setting the train a set sizes
train_size = int(len(dataset) * 0.67) #splitting the set into train set with 67% of the observation
test_size = len(dataset) - train_size #Splitting the set into test set with 33% of the observation (sustracting trainsize)

#Splitting the data
train, test = dataset[0:train_size,:], dataset[train_size:len(dataset),:]#Ordering
print(len(train), len(test))

print("Turning the dataset into a Correlation Matrix")
#I don't understand this shit----------------------

# function that convert an array of values into a dataset matrix (correlation matrix) aka "Reshape to x=t y=t+1"
def create_dataset(dataset, look_back=1):
	dataX, dataY = [], []
	for i in range(len(dataset)-look_back-1):   #I guess this prints the Xrow(t) and the Yrow(t+1)
		a = dataset[i:(i+look_back), 0]
		dataX.append(a)                         #Xrow (t)
		dataY.append(dataset[i + look_back, 0]) #Yrow (t+1)
	return np.array(dataX), np.array(dataY) #Returns your shit ready

#Until here.---------------------------------------

# reshape into X=t and Y=t+1
look_back = 1
trainX, trainY = create_dataset(train, look_back)
testX, testY = create_dataset(test, look_back)
print("Correlation Matrix Created")

print("")
print("Reshaping input data form for LSTM NN")
# reshape input to be [samples, time steps, features]
trainX = np.reshape(trainX, (trainX.shape[0], 1, trainX.shape[1]))
testX = np.reshape(testX, (testX.shape[0], 1, testX.shape[1]))

print("EVA_Prototype3 // DATASETTING PROCESS FINISHED")
print("")
#This is the EVA LSTM NN

print("EVA_Prototype3 // NEURAL NETWORK BUILDING PROCESS STARTED")
print("")
#Keras Imports
from keras.models import load_model
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from keras.activations import relu
from keras.layers import Conv2D
from keras.layers import ConvLSTM2D

# create and fit the LSTM network
model = Sequential()
model.add(LSTM(30, input_shape=(1, look_back)))
model.add(Dense(1, activation='relu'))
model.compile(loss='mean_squared_error', optimizer='SGD')

#Mounting model configuration

model.fit(trainX, trainY, epochs=100, batch_size=1, verbose=2)

#model = load_model(r'C:\Users\Usuario\Documents\GitHub\Leviathan\Leviathan\Fortune Tellers\Models\Eva.h5')

model.save(r'C:\Users\Usuario\Documents\GitHub\Leviathan\Leviathan\Fortune Tellers\Models\Eva_prototype3.h5')  # creates a HDF5 file 'my_model.h5'
print("")
print("EVA_Prototype3 // NEURAL NETWORK BUILDING PROCESS FINISHED")
print("")
print("EVA_Prototype3 // MAKING PREDICTIONS")
print("EVA_Prototype3 // MODE 1")

# make predictions
trainPredict = model.predict(trainX)
testPredict = model.predict(testX)
# invert predictions
trainPredict = scaler.inverse_transform(trainPredict)
trainY = scaler.inverse_transform([trainY])
testPredict = scaler.inverse_transform(testPredict)
testY = scaler.inverse_transform([testY])
# calculate root mean squared error
trainScore = math.sqrt(mean_squared_error(trainY[0], trainPredict[:,0]))
print('Train Score: %.2f RMSE' % (trainScore))
testScore = math.sqrt(mean_squared_error(testY[0], testPredict[:,0]))
print('Test Score: %.2f RMSE' % (testScore))

# shift train predictions for plotting
trainPredictPlot = np.empty_like(dataset)
trainPredictPlot[:, :] = np.nan
trainPredictPlot[look_back:len(trainPredict)+look_back, :] = trainPredict
# shift test predictions for plotting
testPredictPlot = np.empty_like(dataset)
testPredictPlot[:, :] = np.nan
testPredictPlot[len(trainPredict)+(look_back*2)+1:len(dataset)-1, :] = testPredict
# plot baseline and predictions
plt.plot(scaler.inverse_transform(dataset))
plt.plot(trainPredictPlot)
plt.plot(testPredictPlot)
plt.show()
plt.savefig('prediction.png')