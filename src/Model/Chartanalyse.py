"""

### Hier wird die Chartanalyse stehen
##Hier ein weiterer eigentest

#fertiger Code mit jeder menge Indikatoren: https://github.com/bukosabino/ta/blob/master/ta/wrapper.py
pip install ta
16.12.2020
"""

import pandas
import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import pyplot as plt
from ta.trend import ADXIndicator

import yfinance as yf
aapl = yf.download('AAPL', '2017-1-1','2019-12-18')

print(aapl)

aapl['Adj Open'] = aapl.Open * aapl['Adj Close']/aapl['Close']
aapl['Adj High'] = aapl.High * aapl['Adj Close']/aapl['Close']
aapl['Adj Low'] = aapl.Low * aapl['Adj Close']/aapl['Close']
aapl.dropna(inplace=True)

print(aapl['Adj Open'])
print(aapl['Adj High'])
print(aapl['Adj Low'])


from ta.trend import ADXIndicator
adxI = ADXIndicator(aapl['Adj High'],aapl['Adj Low'],aapl['Adj Close'],14,False)
aapl['pos_directional_indicator'] = adxI.adx_pos()
aapl['neg_directional_indicator'] = adxI.adx_neg()
aapl['adx'] = adxI.adx()
aapl.tail()

def plot_graph(data,ylabel,xlabel):
    plt.figure(figsize=(10,7))
    plt.grid()
    plt.plot(data)
    plt.ylabel(ylabel)
    plt.xlabel(xlabel)
plot_graph(aapl['Adj Close'], 'Price', 'Date')
plot_graph(aapl['adx'], 'Price', 'Date')

aapl['trend'] = np.where(aapl.adx>25,aapl['Adj Close'],np.nan)

aapl['trend_signal'] = np.where(aapl.adx>25,1,0)
plt.figure(figsize=(10,7))
plt.grid()
plt.plot(aapl['Adj Close'])
plt.plot(aapl['trend'])
plt.ylabel('Price')
plt.xlabel('Date')

aapl['direction'] = np.where(aapl.pos_directional_indicator>aapl.neg_directional_indicator,1,-1) * aapl['trend_signal']
aapl['daily_returns'] = aapl['Adj Close'].pct_change()
aapl['strategy_returns'] = aapl.daily_returns.shift(-1) * aapl.direction
plot_graph((aapl['strategy_returns']+1).cumprod(), 'Returns', 'Date')



# Mögliche aktienchartanalysen von
# https://de.wikipedia.org/wiki/Technische_Analyse#Technische_Indikatoren

#def macd
    #https://de.wikipedia.org/wiki/MACD

#def dg
    #https://de.wikipedia.org/wiki/Gleitender_Durchschnittspreis

#def adx
    #https://de.wikipedia.org/wiki/Average_Directional_Movement_Index