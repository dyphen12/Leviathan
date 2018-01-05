import requests, json, csv

import boto3

import os

import time

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
	
	print('Bitstory Module v0.5 alpha\n')
	
	print('a history of bitcoin prices\n')
	
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

	h = open("bitstory.txt","a")
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
            with open('amazondata.csv', 'a') as csvfile:               
                fieldnames = ['market_cap', 'price','avlble_spply','volume24h','prcntg_chnge24h']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

                writer.writeheader()
                writer.writerow({'market_cap': cmkdata['market_cap_usd'],
                             'price': cmkdata['price_usd'],
                             'avlble_spply': cmkdata['available_supply'],
                             'volume24h':cmkdata['24h_volume_usd'],
                             'prcntg_chnge24h':cmkdata['percent_change_24h']})
            	
	else:
            with open('amazondata.csv', 'a') as csvfile:
                fieldnames = ['market_cap', 'price','avlble_spply','volume24h','prcntg_chnge24h']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            
                writer.writerow({'market_cap': cmkdata['market_cap_usd'],
                             'price': cmkdata['price_usd'],
                             'avlble_spply': cmkdata['available_supply'],
                             'volume24h':cmkdata['24h_volume_usd'],
                             'prcntg_chnge24h':cmkdata['percent_change_24h']})
	          
	print ("\n\n wait 10 seconds for the next request")
	
	cont = cont+1

	time.sleep(nextreq)
	
	os.system('cls')


    