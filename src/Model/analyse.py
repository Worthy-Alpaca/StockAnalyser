"""
Created on 23.12.2020
@author: Stephan Schumacher

Analyse 
"""

import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
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
        df['38ma'] = df['Adj Close'].rolling(window=38, min_periods=0).mean()

        plot.plot(df.index, df['Adj Close'])
        plot.plot(df.index, df['100ma'])
        plot.plot(df.index, df['38ma'])

        plot.set_title(f"30 & 100 Tage gleitender Durchschnitt von {data.getStock1()}")
        plot.legend(( 'Adj Close', '100ma' ,'38ma'),loc='upper left')

    def plaindata(self, data, plot):
        df = web.DataReader(data.getStock1(), 'yahoo', self.parseDate(data, "start"), self.parseDate(data, "end"))["Adj Close"]
        style.use('ggplot')
        plot.plot(df)

    def candlestick(self, data, plot):

        style.use('ggplot')
        df = web.DataReader(data.getStock1(), 'yahoo', self.parseDate(data, "start"), self.parseDate(data, "end"))

        df_ohlc = df['Adj Close'].resample('10D').ohlc() 
        df_ohlc.reset_index(inplace=True)
        df_ohlc['Date'] = df_ohlc['Date'].map(mdates.date2num)

        plot.xaxis_date()
        plot.set_title(f"Candlesticks von {data.getStock1()}")
        candlestick_ohlc(plot, df_ohlc.values, width=4, colorup='g')

    def volume(self, data, plot):
        style.use('ggplot')
        df = web.DataReader(data.getStock1(), 'yahoo', self.parseDate(data, "start"), self.parseDate(data, "end"))
        plot.bar(df.index, df['Volume'])

    def bollinger(self, data, plot, plot2):

        #https://medium.com/python-data/setting-up-a-bollinger-band-with-python-28941e2fa300'

        style.use('ggplot')
        df = web.DataReader(data.getStock1(), 'yahoo', self.parseDate(data, "start"), self.parseDate(data, "end"))

        df['30 Day MA'] = df['Adj Close'].rolling(window=20).mean()
        df['30 Day STD'] = df['Adj Close'].rolling(window=20).std()

        #Upper Band
        df['Upper Band'] = df['30 Day MA'] + (df['30 Day STD'] * 2)
        
        #Lower Band
        df['Lower Band'] = df['30 Day MA'] - (df['30 Day STD'] * 2)
        
        plot.plot(df[['Upper Band', 'Lower Band']])
        plot2.plot(df[["Adj Close"]])
        plot.set_title(f"30 Tage Bollinger Band {data.getStock1()}")
        plot.legend(('Upper Band', 'Lower Band'),loc='upper left')
        plot2.legend(('30 Day STD'), loc='upper left')

    def volatilität(self, data, plot):

        #https://medium.com/python-data/time-series-aggregation-techniques-with-python-a-look-at-major-cryptocurrencies-a9eb1dd49c1b

        style.use('ggplot')
        df = web.DataReader(data.getStock1(), 'yahoo', self.parseDate(data, "start"), self.parseDate(data, "end"))

        df['30_day_volatility'] = df['Close'].rolling(window=20).std()

        plot.plot(df[['Adj Close', '30_day_volatility']])
        plot.set_title(f"30 Tage Volatilität von {data.getStock1()}")

    def dailyreturns(self, data, plot):
        style.use('ggplot')

        df = pd.DataFrame()
        assets = [data.getStock1(), data.getStock2()]

        for stock in assets:
            df[stock] = web.DataReader(stock, 'yahoo', self.parseDate(data, "start"), self.parseDate(data, "end"))['Adj Close']

        asset_returns_daily = df.pct_change()
        #asset_volatility_daily = asset_returns_daily.std()
        
        plot.plot(asset_returns_daily)
        plot.set_title(f"Daily returns von {data.getStock1()} und {data.getStock2()}")
        plot.legend((data.getStock1(), data.getStock2()), loc='upper left')

    def macd(self, data, plot):

        style.use('ggplot')
        df = web.DataReader(data.getStock1(), 'yahoo', self.parseDate(data, "start"), self.parseDate(data, "end"))
        df['ema12'] = df['Adj Close'].ewm(span=12).mean()
        df['ema26'] = df['Adj Close'].ewm(span=26).mean()
        df['MACD'] = (df['ema12']-df['ema26'])

        df['Signal'] = df['MACD'].ewm(span=9).mean()
        plot.plot(df[['Adj Close', 'MACD', 'Signal']])
        plot.set_title(f"Adj Close MACD und Signallinie von {data.getStock1()}")
        plot.legend(( 'Adj Close','MACD', 'Signal'),loc='upper left')
        #print("Hello")

    def risk(self, data, plot):
        """ mit dailyreturns vergleichen da funktionen die gleichen sind """
        style.use('ggplot')
        #https://medium.com/python-data/assessing-the-riskiness-of-a-single-stock-in-python-12f2c5bb85b2

        
        assets = [data.getStock1(), data.getStock2()]
        df = pd.DataFrame()
        
        for stock in assets:
            df[stock] = web.DataReader(stock, 'yahoo', self.parseDate(data, "start"), self.parseDate(data, "end"))['Adj Close']

        asset_returns_daily = df.pct_change()
        asset_volatility_daily = asset_returns_daily.std()

        asset_volatility_daily.plot.hist(bins=50, figsize=(10,6));
        plot.set_xlabel('Risiko')
        plot.set_title(f"Risiko von {data.getStock1()} und {data.getStock2()}")
        #print("Hello")
        #plot(df())
        #plot.plot(df[['Adj Close', 'Upper Band', 'Lower Band']])

    def rsi(self, data, plot, plot2):

        #https://stackoverflow.com/questions/20526414/relative-strength-index-in-python-pandas

        style.use('ggplot')
        window_length = 14

        df = web.DataReader(data.getStock1(), 'yahoo', self.parseDate(data, "start"), self.parseDate(data, "end"))
        close = df['Adj Close']

        delta = close.diff()
        delta = delta[1:]

        up, down = delta.copy(), delta.copy()
        up[up < 0] = 0
        down[down > 0] = 0

        # Calculate the EWMA
        roll_up1 = up.ewm(span=window_length).mean()
        roll_down1 = down.abs().ewm(span=window_length).mean()

        # Calculate the RSI based on EWMA
        RS1 = roll_up1 / roll_down1
        RSI1 = 100.0 - (100.0 / (1.0 + RS1))

        # Calculate the SMA
        roll_up2 = up.rolling(window_length).mean()
        roll_down2 = down.abs().rolling(window_length).mean()

        # Calculate the RSI based on SMA
        RS2 = roll_up2 / roll_down2
        RSI2 = 100.0 - (100.0 / (1.0 + RS2))

        # Compare graphically
        plot.plot(RSI1)
        plot2.plot(RSI2)
        plot.legend(['RSI via EWMA'])
        plot2.legend(['RSI via SMA'])
        plot.set_ylabel("Something something")

    def adx(self, data, plot, plot2):
        #gibt die Stärke eines Trendes an
        style.use('ggplot')
        df = web.DataReader(data.getStock1(), 'yahoo', self.parseDate(data, "start"), self.parseDate(data, "end"))

        df['Adj Open'] = (df['Open']*df['Adj Close']/df['Close'])
        df['Adj High'] = (df['High']*df['Adj Close']/df['Close'])
        df['Adj Low'] = (df['Low']*df['Adj Close']/df['Close'])

        df['DX'] = (()/()).rolling(window=14).mean() #funktion noch nicht fertig
        pass








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
    data.setStartDate("2010-12-12")
    data.setEndDate("2020-12-12")
    plot = plt.subplot2grid((6, 1), (0, 0), rowspan=5, colspan=1)
    test = Analyse()
    #test.durchschnitt(data, plot)
    #test.candlestick(data, plot)
    #test.bollinger(data, plot)
    #test.volume(data, plot)
    #test.volatilität(data, plot)
    #test.dailyreturns(data)
    #test.risk(data, plot) #muss noch optimiert werden
    #test.macd(data, plot)
    #test.adx(data, plot) #noch nicht fertig
    plt.show()
