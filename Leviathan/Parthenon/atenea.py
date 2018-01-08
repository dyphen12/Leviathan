'Made by Dyphen12'
'07/07/18'

'-------------------'

import ccxt
from Pilots.asukav2 import LonginosSpear

'Atenea the justice goddess'

print('Atenea Module\n')

print('Cryptocurrencies Trading System Module for a secure trading\n')

print('This module works with Bitmex\n')

print('This module is receiving data from the pilot "Asuka"\n')

#starting the module

(prediction,realdata)=LonginosSpear()
print(prediction)
print(realdata[-1])

print('This prediction is for the next 10 minutes aprox.\n')
'NOTE: Check the yuxtaposition of data and trainsets timesteps problem I or the problem with the data time'

print('ATENEA IS ON // Now checking BitMEX account\n')

'NOTE: Note that the module is in development so were gonna print your API Key and your Security Key'

bitmex = ccxt.bitmex({
    'apiKey': 'vMLpmDjetlFudTTYXFRibN3c',
    'secret': '-pG3_-pEQjw0WGbTQ7gt8xMDHMY2oHSIUQA7vP8sfxgnNbR9',
})
print('ATENEA // BitMEX account loaded\n')
print('ATENEA // Hello Im Atenea the security Goddess.\n')

print('ATENEA // Now im going to load the current SAFE TRADING algorithm\n')

def safetrading ():
    print('Your algorithm goes here! :)')
    return

print('The Algorithm is loaded, do you want to execute it?\n')

print('1-Yes')
print('2-No')

option=int(input())

if option==1:
    safetrading()
elif option==2:
    print('Ok sorry')






