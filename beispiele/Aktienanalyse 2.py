# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 20:23:38 2020

@author: Yannic
"""
# dies ist ein kommentar
#$ conda install -c ranaroussi yfinance
from matplotlib import pyplot as plt
# import pandas as pd
import yfinance as yf
# from datetime import datetime
# from time import time

apple = yf.Ticker("AAPL") #Appleaktie
# google = yf.Ticker("GOOG")
# etf1 = yf.Ticker("ZPRX.DE")
# etf2 = yf.Ticker("XWD.TO")
# msft = yf.Ticker("MSFT")

print(apple.history(start=("2019-02-01"), end=("2019-03-07")))
# print(google.history(start=("2019-02-01"), end=("2019-03-07")))
# print(etf1.history(start=("2019-02-01"), end=("2019-03-07")))
# print(etf2.history(start=("2019-02-01"), end=("2019-03-07")))
# print(msft.history(start=("2019-02-01"), end=("2019-03-07")))

data = yf.download(("AAPL") , start="2019-02-01", end="2019-02-25")

plt.figure()
data["Close"].plot()     #es funktioniert nicht Close und Open in ein Diagram zu plotten
data["Open"].plot()
plt.title("Apple")
plt.legend()



# data = yf.download("AAPL", start="x", end="y", interval="15m")

# x = time('%20-%11-%17')
# y = time('year(2020)', 'month(11)','day(17)','hours(14)')
# '%2020'-'%11'-'%17'-'%10'

# x = datetime.datetime(2020, 11, 17, 10, 0, 0)
# y = datetime.datetime(2020, 11, 17, 12, 0, 0)

# plt.figure()
# data["Close"].plot()
# data["Open"].plot()
# plt.title("ETF1  Chart")
# plt.legend()

# data = yf.download("XWD.TO", start="2019-02-01", end="2019-02-25")

# plt.figure()
# data["Close"].plot()
# data["Open"].plot()
# plt.title("ETF 2")
# plt.legend()

# data = yf.download("GOOG", start="2020-11-24", end="2020-11-25", interval="1m")

# plt.figure()
# #data["Close"].plot()
# data["Open"].plot()
# plt.title("GOOGLE Chart")
# plt.legend()


# #Open und Close Tageswerte
# data = yf.download("MSFT", start="2018-03-01", end="2019-02-13")

# plt.figure()
# data["Close"].plot()
# data["Open"].plot()
# plt.title("MSFT Chart")
# plt.legend()

# #Open und Close der Minutenwerte
# # x =
# data = yf.download("MSFT", start="2020-11-17_00-10", end="2020-11-18_00-15", interval="1m")

# plt.figure()
# data["Close"].plot()
# data["Open"].plot()
# plt.title("MSFT Chart")
# plt.legend()


# data = yf.download(("XWD.TO", "ZPRX.DE") , start="2019-11-01", end="2020-11-24")


# plt.figure()
# data["Close"].plot()     #es funktioniert nicht Close und Open in ein Diagram zu plotten
# # data["Open"].plot()
# plt.title("ETF's Chart")
# plt.legend()