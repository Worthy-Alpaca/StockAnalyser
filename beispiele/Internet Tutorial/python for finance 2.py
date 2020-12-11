"""
Tutorials
11.12.2020
"""
import datetime as dt
import matplotlib.pyplot as plt     # erlaupt zu plotten
from matplotlib import style        # so sieht es besser aus
import pandas as pd
import pandas_datareader.data as web

style.use('ggplot')

#start = dt.datetime(2000,1,1)
#end = dt.datetime(2016,12,31)

#df = web.DataReader('TSLA', 'yahoo', start, end)        #holt sich daten aus zeile 9, TSLA der Ticker von Tesla
#df.to_csv('tsla.csv')

df = pd.read_csv('tsla.csv', parse_dates=True, index_col=0)

#print(df.head())
print(df[['Open','High']].head())

df['Adj Close'].plot()
plt.show()
