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

print("EVA_Prototype2")
print("")
print("Initializing...")
print("")
print("EVA_Prototype2 // ON")

#Analyze of the dataset
print("Getting dataset // NOW USING: pandas")

Location = r'C:\Users\Usuario\Documents\GitHub\Leviathan\Leviathan\Fortune Tellers\Datasets\Eva prototype\BTCUSD_Coindesk.csv'
dataframe = pd.read_csv(Location,usecols=[1], engine='python', skipfooter=1)

dataset = dataframe.values
dataset = dataset.astype('float32')

print("Dataset loaded!")

import matplotlib.pyplot as plt

plt.plot(dataset)
plt.show()