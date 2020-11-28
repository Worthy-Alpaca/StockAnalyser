# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 14:29:43 2020

@author: Yannic
"""

import pandas as pd

data = pd.read_csv("C:/Users/Yannic/OneDrive/Dokumente/Technische Hochschule Lübeck/Projekt Digitale Wirtschaft/aapl.csv")

# x = ['Date', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']
print(data.columns)
print(data.shape)


print(data)