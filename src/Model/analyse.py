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

    """ def parseData(self, data):
        
        return start, end """


    def durchschnitt(self, data):
        startDate = data.getStartDate()
        endDate = data.getEndDate()

        start = dt.datetime(startDate[0], startDate[1], startDate[2])
        end = dt.datetime(endDate[0], endDate[1], endDate[2])
        #test = self.parseData(data)

        df = web.DataReader(data.getStock1(), 'yahoo', start, end)
        style.use('ggplot')

        df['100ma'] = df['Adj Close'].rolling(
            window=100, min_periods=0).mean()        # 100 Average
        df['38ma'] = df['Adj Close'].rolling(
            window=38, min_periods=0).mean()           # 38  Average

        print(df.head())

        ax1 = plt.subplot2grid((6, 1), (0, 0), rowspan=5, colspan=1)
        ax1.plot(df.index, df['Adj Close'])
        ax1.plot(df.index, df['100ma'])
        ax1.plot(df.index, df['38ma'])

        plt.show()

    def candlestick(self,data):
        startDate = data.getStartDate()
        endDate = data.getEndDate()

        start = dt.datetime(startDate[0], startDate[1], startDate[2])
        end = dt.datetime(endDate[0], endDate[1], endDate[2])

        style.use('ggplot')
        df = web.DataReader(data.getStock1(), 'yahoo', start, end)

        df_ohlc = df['Adj Close'].resample('10D').ohlc() 
        df_ohlc.reset_index(inplace=True)
        df_ohlc['Date'] = df_ohlc['Date'].map(mdates.date2num)

        print(df_ohlc.head)

        ax1 = plt.subplot2grid((6,1), (0,0), rowspan=5, colspan=1)
        ax1.xaxis_date()
        candlestick_ohlc(ax1, df_ohlc.values, width=4, colorup='g')

        plt.show()
        #print("Hallo")

    def volume(self,data):
        startDate = data.getStartDate()
        endDate = data.getEndDate()

        start = dt.datetime(startDate[0], startDate[1], startDate[2])
        end = dt.datetime(endDate[0], endDate[1], endDate[2])

        style.use('ggplot')
        df = web.DataReader(data.getStock1(), 'yahoo', start, end)

        print(df.head())

        ax1 = plt.subplot2grid((6,1), (0,0), rowspan=5, colspan=1)
        ax1.bar(df.index, df['Volume'])

        plt.show()

    def bollinger(self,data):

        #https://medium.com/python-data/setting-up-a-bollinger-band-with-python-28941e2fa300'

        startDate = data.getStartDate()
        endDate = data.getEndDate()

        start = dt.datetime(startDate[0], startDate[1], startDate[2])
        end = dt.datetime(endDate[0], endDate[1], endDate[2])

        style.use('ggplot')
        df = web.DataReader(data.getStock1(), 'yahoo', start, end)

        df['30 Day MA'] = df['Adj Close'].rolling(window=20).mean()
        df['30 Day STD'] = df['Adj Close'].rolling(window=20).std()

        #Upper Band
        df['Upper Band'] = df['30 Day MA'] + (df['30 Day STD'] * 2)
        
        #Lower Band
        df['Lower Band'] = df['30 Day MA'] - (df['30 Day STD'] * 2)
        
        df[['Adj Close', 'Upper Band', 'Lower Band']].plot(figsize=(12,6))
        #df[['Adj Close', '30 Day MA', 'Upper Band', 'Lower Band']].plot(figsize=(12,6))
        plt.title(f"30 Tage Bollinger Band {data.getStock1()}" )
        plt.ylabel('Price (USD)')
        plt.show()


        
    def volatilität(self,data):

        #https://medium.com/python-data/time-series-aggregation-techniques-with-python-a-look-at-major-cryptocurrencies-a9eb1dd49c1b

        startDate = data.getStartDate()
        endDate = data.getEndDate()

        start = dt.datetime(startDate[0], startDate[1], startDate[2])
        end = dt.datetime(endDate[0], endDate[1], endDate[2])

        style.use('ggplot')
        df = web.DataReader(data.getStock1(), 'yahoo', start, end)

        df['30_day_volatility'] = df['Close'].rolling(window=20).std()

        df[['Adj Close', '30_day_volatility']].plot(figsize=(10,8))
        plt.title(f"30 Tage Volatilität von {data.getStock1()}")
        plt.ylabel('Price')
        plt.show()


    def dailyreturns(self,data):
        startDate = data.getStartDate()
        endDate = data.getEndDate()

        start = dt.datetime(startDate[0], startDate[1], startDate[2])
        end = dt.datetime(endDate[0], endDate[1], endDate[2])

        style.use('ggplot')
        #df = web.DataReader(data.getStock1(), 'yahoo', start, end)

        df = pd.DataFrame()
        assets = [data.getStock1(), data.getStock2()]

        for stock in assets:
            df[stock] = web.DataReader(stock,'yahoo', start, end)['Adj Close']

        asset_returns_daily = df.pct_change()
        asset_volatility_daily = asset_returns_daily.std()

        asset_returns_daily.plot.hist(bins=50, figsize=(10,6));
        plt.xlabel('Daily Returns')
        plt.show()

        








if __name__ == "__main__":
    #sys.path.append("C:/Users/Yannic/OneDrive/Dokumente/Technische Hochschule Lübeck/Projekt Digitale Wirtschaft/diwi4/src/" + "basic_io")
    sys.path.append("C:/Users/Nils/Desktop/AllesMögliche/TH/5.Semester/DiWi/diwi4/src/" + "basic_io")
    from basic_io import Input
    data = Input()
    data.setFirstStock("AAPL")
    data.setSecondStock("GOOGL")
    data.setStartDate("2018-12-12")
    data.setEndDate("2020-12-12")
    test = Analyse()
    #test.durchschnitt(data)
    #test.candlestick(data)
    #test.bollinger(data)
    #test.volume(data)#
    #test.volatilität(data)
    #test.dailyreturns(data)