"""
Created on 23.12.2020
@author: Stephan Schumacher

Analyse 
"""

import datetime as dt
import matplotlib.pyplot as plt     # erlaupt zu plotten
from matplotlib import style        # so sieht es besser aus
import pandas as pd
import pandas_datareader.data as web
import sys

#Import Candlestick
import mplfinance
import matplotlib.dates as mdates
from mplfinance.original_flavor import candlestick_ohlc 

class Analyse:
    def __init__(self):
        pass
    
    def parseDate(self, data, x):
        if x == "start":
            startDate = data.getStartDate()
            start = dt.datetime(startDate[0], startDate[1], startDate[2])
            return start
        else:
            endDate = data.getEndDate()
            end = dt.datetime(endDate[0], endDate[1], endDate[2])
            return end
    
    def durchschnitt(self, data, plot):
        df = web.DataReader(data.getStock1(), 'yahoo', self.parseDate(data, "start"), self.parseDate(data, "end"))
        style.use('ggplot')

        df['100ma'] = df['Adj Close'].rolling(window=100, min_periods=0).mean()        # 100 Average
        df['38ma'] = df['Adj Close'].rolling(window=38, min_periods=0).mean()           # 38  Average

        plot.plot(df.index, df['Adj Close'])
        plot.plot(df.index, df['100ma'])
        plot.plot(df.index, df['38ma'])

        plot.set_title(f"30 & 100 Tage gleitender Durchschnitt von {data.getStock1()}")
        plot.set_ylabel('Price')
        plot.legend(( 'Adj Close', '100ma' ,'38ma'),loc='upper left')

    def candlestick(self, data, plot):

        style.use('ggplot')
        df = web.DataReader(data.getStock1(), 'yahoo', self.parseDate(data, "start"), self.parseDate(data, "end"))

        df_ohlc = df['Adj Close'].resample('10D').ohlc() 
        df_ohlc.reset_index(inplace=True)
        df_ohlc['Date'] = df_ohlc['Date'].map(mdates.date2num)

        plot.xaxis_date()
        plot.set_title(f"Candlesticks von {data.getStock1()}")
        plot.set_ylabel('Price')
        candlestick_ohlc(plot, df_ohlc.values, width=4, colorup='g')

    def volume(self, data, plot):
        style.use('ggplot')
        df = web.DataReader(data.getStock1(), 'yahoo', self.parseDate(data, "start"), self.parseDate(data, "end"))
        plot.bar(df.index, df['Volume'])

    def bollinger(self, data, plot):

        #https://medium.com/python-data/setting-up-a-bollinger-band-with-python-28941e2fa300'

        style.use('ggplot')
        df = web.DataReader(data.getStock1(), 'yahoo', self.parseDate(data, "start"), self.parseDate(data, "end"))

        df['30 Day MA'] = df['Adj Close'].rolling(window=20).mean()
        df['30 Day STD'] = df['Adj Close'].rolling(window=20).std()

        #Upper Band
        df['Upper Band'] = df['30 Day MA'] + (df['30 Day STD'] * 2)
        
        #Lower Band
        df['Lower Band'] = df['30 Day MA'] - (df['30 Day STD'] * 2)
        
        plot.plot(df[['Adj Close', 'Upper Band', 'Lower Band']])
        #df[['Adj Close', '30 Day MA', 'Upper Band', 'Lower Band']].plot(figsize=(12,6))
        plot.set_title(f"30 Tage Bollinger Band {data.getStock1()}")
        plot.set_ylabel('Price (USD)')
        plot.legend(( '30 Day STD','Upper Band', 'Lower Band'),loc='upper left')

    def volatilität(self, data, plot):

        #https://medium.com/python-data/time-series-aggregation-techniques-with-python-a-look-at-major-cryptocurrencies-a9eb1dd49c1b

        style.use('ggplot')
        df = web.DataReader(data.getStock1(), 'yahoo', self.parseDate(data, "start"), self.parseDate(data, "end"))

        df['30_day_volatility'] = df['Close'].rolling(window=20).std()

        plot.plot(df[['Adj Close', '30_day_volatility']])
        plot.set_title(f"30 Tage Volatilität von {data.getStock1()}")
        plot.set_ylabel('Price')


    def dailyreturns(self,data):
        style.use('ggplot')
        #df = web.DataReader(data.getStock1(), 'yahoo', start, end)

        df = pd.DataFrame()
        assets = [data.getStock1(), data.getStock2()]

        for stock in assets:
            df[stock] = web.DataReader(stock, 'yahoo', self.parseDate(data, "start"), self.parseDate(data, "end"))['Adj Close']

        asset_returns_daily = df.pct_change()
        asset_volatility_daily = asset_returns_daily.std()

        asset_returns_daily.plot.hist(bins=50, figsize=(10,6));
        plt.xlabel('Daily Returns')
        plt.show()

    
    def macd(self,data):
        startDate = data.getStartDate()
        endDate = data.getEndDate()

        start = dt.datetime(startDate[0], startDate[1], startDate[2])
        end = dt.datetime(endDate[0], endDate[1], endDate[2])

        style.use('ggplot')
        df = web.DataReader(data.getStock1(), 'yahoo', start, end)

        
        print(df)








if __name__ == "__main__":
    #sys.path.append("C:/Users/Yannic/OneDrive/Dokumente/Technische Hochschule Lübeck/Projekt Digitale Wirtschaft/diwi4/src/" + "basic_io")
    #sys.path.append("C:/Users/Nils/Desktop/AllesMögliche/TH/5.Semester/DiWi/diwi4/src/" + "basic_io")
    #sys.path.append("C:/Users/Stephan/source/repos/diwi4/src/" + "basic_io")
    #sys.path.append("C:/Users/Yannic/OneDrive/Dokumente/Technische Hochschule Lübeck/Projekt Digitale Wirtschaft/diwi4/src/" + "basic_io")
    #sys.path.append("C:/Users/Nils/Desktop/AllesMögliche/TH/5.Semester/DiWi/diwi4/src/" + "basic_io")
    from basic_io import Input
    data = Input()
    data.setFirstStock("AAPL")
    data.setSecondStock("GOOGL")
    data.setStartDate("2018-12-12")
    data.setEndDate("2020-12-12")
    plot = plt.subplot2grid((6, 1), (0, 0), rowspan=5, colspan=1)
    test = Analyse()
    #test.durchschnitt(data, plot)
    #test.candlestick(data, plot)
    #test.bollinger(data, plot)
    #test.volume(data, plot)
    #test.volatilität(data, plot)
    #test.dailyreturns(data)
    plt.show()
