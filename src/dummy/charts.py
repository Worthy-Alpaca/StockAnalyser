import datetime as dt
import matplotlib.pyplot as plt     # erlaupt zu plotten
from matplotlib import style        # so sieht es besser aus
import pandas as pd
import pandas_datareader.data as web
import sys
import json
import yfinance as yf

class DummyCharts:
    def __init__(self):
        pass
    
    def chart(self, data, figure):
        style.use('ggplot')
        startDate = data.getStartDate()
        endDate = data.getEndDate()       
        
        start = dt.datetime(startDate[0], startDate[1], startDate[2])
        end = dt.datetime(endDate[0], endDate[1], endDate[2])
        print(start)
        #df = web.DataReader(data.getStock1(), 'yahoo', start, end)
        df = yf.download((data.getStock1(), data.getStock2()), start=start, end=end)
        # df = pd.read_csv('tsla.csv', parse_dates=True, index_col=0)
        #df['100ma'] = df['Adj Close'].rolling(
            #window=100, min_periods=0).mean()        # 100 Average
        #df['38ma'] = df['Adj Close'].rolling(
            #window=38, min_periods=0).mean()          # 38  Average
        print(df)
        figure.add_subplot(111).plot(df.index, df['Close'])
        #figure.add_subplot().plot(df.index, df['Open'])
        #figure.add_subplot(111).plot(df.index, df['Adj Close'])
        #figure.add_subplot(111).plot(df.index, df['100ma'])
        #figure.add_subplot(111).plot(df.index, df['38ma'])
        #figure.add_subplot(111).bar(df.index, df['Volume'])
        """
        ax1 = plt.subplot2grid((6, 1), (0, 0), rowspan=5, colspan=1)
        ax2 = plt.subplot2grid((6, 1), (5, 0), rowspan=1, colspan=1, sharex=ax1)

        ax1.plot(df.index, df['Adj Close'])
        ax1.plot(df.index, df['100ma'])
        ax1.plot(df.index, df['38ma'])
        ax2.bar(df.index, df['Volume'])
        return plt
        #plt.show()"""
