# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 12:47:45 2020

@author: Yannic
"""
#from datetime import
# import pandas as pd
import yfinance as yf
from matplotlib import pyplot as plt


class Model:
    def __init__(self, name, start, end, interval):
        self.name = name
        self.start = start
        self.end = end
        self.interval = interval
        
    def getName(self):
        return self.name
    
    def getStart(self):
        return self.start
    
    def getEnd(self):
        return self.end
    
    def getInterval(self):
        return self.interval
    
Aktienkurs = input("Geben Sie das Unternehmen an")
Startwert = input("Geben Sie den Startwert an in JAHR-Monat-Tag") 
Endwert = input("Geben Sie den Endwert an in JAHR-Monat-Tag")
Interval = input("Geben Sie ein Interval an")   
 
if __name__=="__main__":
    Aktie = Model(Aktienkurs, Startwert, Endwert, Interval)


# print(Aktie.start)

# print(Aktienkurs)

data = yf.download(Aktienkurs, Startwert, Endwert, Interval)

plt.figure()
#data["Close"].plot()
data["Open"].plot()
plt.title(Aktienkurs)
plt.legend()
