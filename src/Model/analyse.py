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


if __name__ == "__main__":
    sys.path.append("hier _path aus config.py ein setzen" + "basic_io")
    from basic_io import Input
    data = Input()
    data.setFirstStock("AAPL")
    data.setSecondStock("GOOGL")
    data.setStartDate("2012-12-12")
    data.setEndDate("2020-12-12")
    test = Analyse().durchschnitt(data)
