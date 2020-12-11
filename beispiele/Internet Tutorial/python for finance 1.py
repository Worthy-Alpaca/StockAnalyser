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

start = dt.datetime(2010,1,1)
end = dt.datetime(2016,12,31)

df = web.DataReader('TSLA', 'yahoo', start, end)          #holt sich daten aus zeile 9, TSLA der Ticker von Tesla
df.reset_index(inplace=True)
df.set_index("Date", inplace=True)
# df = df.drop('Symbol', axis=1)

print(df.head())