# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 14:29:43 2020

@author: Yannic
"""

import pandas as pd
import json

with open('config.json') as file:
    config = json.load(file)


data = pd.read_csv(config["datapath"]) # der dateipfad muss jetzt in config.json eingesetzt werden.
# x = ['Date', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']
print(data.columns)
print(data.shape)


print(data)
