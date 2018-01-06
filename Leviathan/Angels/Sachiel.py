import requests, json, csv

import os

import time

import numpy as np

from datetime import datetime

cont = 0

option = 2
nextreq = 10;

while option != 0:


	#Time module

	now = datetime.now()

	year=str(now.year)
	month=str(now.month)
	day=str(now.day)

	hour=str(now.hour)
	min=str(now.minute)
	secs=str(now.second)


	#GET request


	print('\nANGEL: SACHIEL\n')

	print('BTC/USD Chart messenger for predictions\n')

	r = requests.get('https://api.coinmarketcap.com/v1/ticker/bitcoin/', timeout=300)

	print('This is the URL')

	print(r.url)

	r.json()

	r.text

	#Decoding JSON

	cmkdatajson = r.text

	cmkdataparsed = json.loads(cmkdatajson)

	cmkdata = cmkdataparsed[0]


	#Print in screen

	print ('\n')

	print ("Request made ", day,"/",month,"/",year," @ ",hour,":",min,":",secs)

	print ('\n')

	print('Crypto:' ,cmkdata['name'])

	print('Market Cap: ','$',cmkdata['market_cap_usd'])

	print('Price: ','$',cmkdata['price_usd'])

	print('Circulating Supply: ',cmkdata['available_supply'], 'BTC')

	print('% Change (24h): ',cmkdata['percent_change_24h'],'%')

	#Write in .txt

	h = open("Sachiel_BTCUSD.txt","a")
	h.write("-------------\n")
	h.write(day)
	h.write("/")
	h.write(month)
	h.write("/")
	h.write(year)
	h.write(" @ ")
	h.write(hour)
	h.write(":")
	h.write(min)
	h.write(":")
	h.write(secs)
	h.write("\n\n")
	h.write('Crypto: ')
	h.write(cmkdata['name'])
	h.write('\n')
	h.write('Market Cap: ')
	h.write('$')
	h.write(cmkdata['market_cap_usd'])
	h.write('\n')
	h.write('Price: ')
	h.write('$')
	h.write(cmkdata['price_usd'])
	h.write('\n')
	h.write('Circulating Supply: ')
	h.write(cmkdata['available_supply'])
	h.write(' BTC')
	h.write('\n')
	h.write('% Change (24h): ')
	h.write(cmkdata['percent_change_24h'])
	h.write('%')
	h.write('\n')
	h.write("\n")
	h.write("-------------")

	h.close()

	#Write in the CSV

	cmplxdata = [cmkdata['market_cap_usd'],
                     cmkdata['price_usd'],
                     cmkdata['available_supply'],
                     cmkdata['24h_volume_usd'],
                     cmkdata['percent_change_24h']]

	if cont == 0:
            with open('BTCUSD.csv', 'a') as csvfile:
                fieldnames = ['day','price']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

                writer.writeheader()
                writer.writerow({
					'day': day,
					'price': cmkdata['price_usd']})

	else:
            with open('BTCUSD.csv', 'a') as csvfile:
                fieldnames = ['day','price']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writerow({
					'day': day,
					'price': cmkdata['price_usd']})

	print ("\n\n wait 10 seconds for the next request")

	cont = cont+1

	time.sleep(nextreq)

	os.system('cls')

	print("EVA RECOGNIZED // PREPARING DATA\n")

	with open('BTCUSDtoEVA.csv', 'a') as csvfile:
		writer = csv.writer(csvfile,quoting=csv.QUOTE_ALL)
		writer.writerow({cmkdata['price_usd'],day})

	import pandas as pd
	import matplotlib.pyplot as plt
	from sklearn.preprocessing import MinMaxScaler

	Location = r'C:\Users\Usuario\Documents\GitHub\Leviathan\Leviathan\Angels\BTCUSDtoEVA.csv'
	dataframe = pd.read_csv(Location, usecols=[1], engine='python')

	dataset = dataframe.values
	dataset = dataset.astype('float32')

	print("Plotting dataset")
	plt.plot(dataset)
	#plt.show()
	print("Dataset plotted")

	# normalize the dataset
	print("Normalizing dataset...")
	scaler = MinMaxScaler(feature_range=(0, 1))
	dataset = scaler.fit_transform(dataset)

	# split into train and test sets

	# Setting the train a set sizes
	train_size = int(len(dataset) * 0.67)  # splitting the set into train set with 67% of the observation
	test_size = len(
		dataset) - train_size  # Splitting the set into test set with 33% of the observation (sustracting trainsize)

	# Splitting the data
	train, test = dataset[0:train_size, :], dataset[train_size:len(dataset), :]  # Ordering
	print(len(train), len(test))

	print("Turning the dataset into a Correlation Matrix")


	# I don't understand this shit----------------------

	# function that convert an array of values into a dataset matrix (correlation matrix) aka "Reshape to x=t y=t+1"
	def create_dataset(dataset, look_back=1):
		dataX, dataY = [], []
		for i in range(len(dataset) - look_back - 1):  # I guess this prints the Xrow(t) and the Yrow(t+1)
			a = dataset[i:(i + look_back), 0]
			dataX.append(a)  # Xrow (t)
			dataY.append(dataset[i + look_back, 0])  # Yrow (t+1)
		return np.array(dataX), np.array(dataY)  # Returns your shit ready


	# Until here.---------------------------------------

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




