# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 17:32:32 2020

@author: ypaul

Aktienanalyse
"""
#$ conda install -c ranaroussi yfinance
from matplotlib import pyplot as plt
# import pandas as pd
import yfinance as yf
import json

###dies ist ein test

with open('config.json') as file:
    config = json.load(file)

apple = yf.Ticker("AAPL")
google = yf.Ticker("GOOG")
etf1 = yf.Ticker("ZPRX.DE")
etf2 = yf.Ticker("XWD.TO")
msft = yf.Ticker("MSFT")

print(apple.history(start=("2019-02-01"), end=("2019-03-07")))
# print(google.history(start=("2019-02-01"), end=("2019-03-07")))
# print(etf1.history(start=("2019-02-01"), end=("2019-03-07")))
# print(etf2.history(start=("2019-02-01"), end=("2019-03-07")))
# print(msft.history(start=("2019-02-01"), end=("2019-03-07")))

# data = yf.download(("AAPL", "ZPRX.DE") , start="2019-02-01", end="2019-02-25")


# plt.figure()
# data["Close"].plot()     #es funktioniert nicht Close und Open in ein Diagram zu plotten
# data["Open"].plot()
# plt.title("Apple und ETF Chart")
# plt.legend()

data = yf.download("ZPRX.DE", start="2014-02-01", end="2019-02-25")

plt.figure()
# data["Close"].plot()
data["Open"].plot()
plt.title("ETF1  Chart")
plt.legend()

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
# data = yf.download("MSFT", start="2020-11-17", end="2020-11-18", interval="1m")

# plt.figure()
# data["Close"].plot()
# data["Open"].plot()
# plt.title("MSFT Chart 1 Minute")
# plt.legend()


# data = yf.download(("XWD.TO", "ZPRX.DE") , start="2019-11-01", end="2020-11-24")


# plt.figure()
# data["Close"].plot()     #es funktioniert nicht Close und Open in ein Diagram zu plotten
# # data["Open"].plot()
# plt.title("ETF's Chart")
# plt.legend()


