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

Location = r'C:\Users\Usuario\Documents\GitHub\Leviathan\Leviathan\Fortune Tellers\Datasets\Eva prototype\BTCUSD_ALL.csv'
df = pd.read_csv(Location)

print("Dataset loaded!")

print("Splitting the data")

train_labels=np.array(df.date)
train_samples=np.array([df.open,df.high,df.low,df.close])

print("Data successfully splitted!")
print("")
print("")
print("PREPROCESSING DATA FOR: Multilayer Perceptron")
print("")
print("STARTING...")

'This is how we process the data for a multilayer perceptron'
scaler = MinMaxScaler(feature_range=(0, 1))
scaled_train_samples = scaler.fit_transform(train_samples)
'That s it!'

print("DATA PROCESSED")
print("")
print("EVA_prototype // STARTING BUILDING NN")






