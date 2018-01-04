#Basic Deep Learning Neural Network "EVA"

#The first functional EVA for Leviathan -- NON FUCTIONAL

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

print("EVA_Prototype2")
print("")
print("Initializing...")
print("")
print("EVA_Prototype2 // ON")

#Analyze of the dataset
print("Getting dataset // NOW USING: pandas")

Location = r'C:\Users\Usuario\Documents\GitHub\Leviathan\Leviathan\Fortune Tellers\Datasets\Eva prototype\BTCUSD_Coindesk.csv'
df = pd.read_csv(Location)

print("Dataset loaded!")

print("Plotting the data")

x = np.array(df.date)
y = np.array(df.close)

trace = go.Scatter(
    x = x,
    y = y
)

data = [trace]

py.offline.plot(data, filename='btcusd.html')
print("PREPROCESSING DATA FOR: Multilayer Perceptron")
print("")
print("STARTING...")

print("Splitting the data")
#Splitting mode 1
X,Y = df

train, test = X[0:-1], Y[-1:]
#Splitting mode 2
seed = 9
np.random.seed(seed)

(X_train, X_test, Y_train, Y_test) = train_test_split(x, y, test_size=0.33, random_state=seed)
print("Data successfully splitted")

print("DATA PROCESSED")
print("")
print("EVA_prototype // STARTING BUILDING NN")

#This is EVA


# imports

from keras.models import Sequential
from keras.layers import Activation
from keras.layers.core import Dense
from keras.optimizers import Adam
from keras.metrics import categorical_crossentropy

# create the model
model = Sequential([
    Dense(32, input_shape=(1,)),
    Dense(6,activation='relu'),
    Dense(1, activation='softmax')
])

# compile the model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# fit the model
model.fit(X_train, Y_train, validation_data=(X_test, Y_test), epochs=100, batch_size=5)