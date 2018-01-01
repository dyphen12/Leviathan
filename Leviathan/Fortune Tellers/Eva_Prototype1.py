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


# seed for reproducing same results
seed = 9
np.random.seed(seed)

# convert series to supervised learning
def series_to_supervised(data, n_in=1, n_out=1, dropnan=True):
	n_vars = 1 if type(data) is list else data.shape[1]
	df = DataFrame(data)
	cols, names = list(), list()
	# input sequence (t-n, ... t-1)
	for i in range(n_in, 0, -1):
		cols.append(df.shift(i))
		names += [('var%d(t-%d)' % (j+1, i)) for j in range(n_vars)]
	# forecast sequence (t, t+1, ... t+n)
	for i in range(0, n_out):
		cols.append(df.shift(-i))
		if i == 0:
			names += [('var%d(t)' % (j+1)) for j in range(n_vars)]
		else:
			names += [('var%d(t+%d)' % (j+1, i)) for j in range(n_vars)]
	# put it all together
	agg = concat(cols, axis=1)
	agg.columns = names
	# drop rows with NaN values
	if dropnan:
		agg.dropna(inplace=True)
	return agg

print("EVA_Prototype")
print("")
print("Initializing...")
print("")
print("EVA_Prototype // ON")

#Analyze of the dataset
print("Getting dataset // NOW USING: pandas")

Location = r'C:\Users\Usuario\Documents\GitHub\Leviathan\Leviathan\Fortune Tellers\Datasets\Eva prototype\ETHBTC.csv'
df = pd.read_csv(Location)

print("Dataset loaded")


#Prepare the dataset
print("Starting preprocessing of the dataset")
print("Converting dataset into a numpy array")

dataset=df
values = dataset.values

encoder = LabelEncoder()
values[:,4] = encoder.fit_transform(values[:,4])

# normalize features
scaler = MinMaxScaler(feature_range=(0, 1))
scaled = scaler.fit_transform(values)

# frame as supervised learning
reframed = series_to_supervised(scaled, 1, 1)
# drop columns we don't want to predict
reframed.drop(reframed.columns[[9,10,11,12,13,14,15]], axis=1, inplace=True)
print(reframed.head())

print(type(dataset))

print("Dataset converted")

print ("Splitting dataset")



