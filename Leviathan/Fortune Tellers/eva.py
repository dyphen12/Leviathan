#Eva the recurrent fortune teller of the btc-usd change


import pandas as pd

import plotly as py

import plotly.graph_objs as go

Location = r'C:\Users\Usuario\Documents\GitHub\Leviathan\Leviathan\Fortune Tellers\Datasets\Eva knowledge\BTCCandlestickdata.csv'
df = pd.read_csv(Location)


trace = go.Candlestick(x=df.index,
                       open=df.open,
                       high=df.high,
                       low=df.low,
                       close=df.close)
data = [trace]
py.offline.plot(data, filename='simple_candlestick.html')

print(df)
