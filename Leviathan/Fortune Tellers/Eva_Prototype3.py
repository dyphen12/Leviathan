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

'Note: The dataset needs to be plotted by matplotlib, if is plotted then works.'

import matplotlib.pyplot as plt

print("Plotting dataset")
plt.plot(dataset)
plt.show()
print("Dataset plotted")

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

