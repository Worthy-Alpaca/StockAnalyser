"""
Tutorials
11.12.2020
"""
import datetime as dt
import matplotlib.pyplot as plt     # erlaupt zu plotten
from matplotlib import style        # so sieht es besser aus
import pandas as pd
import pandas_datareader.data as web

#style.use('ggplot')

#startstock1 =data.getstartdate()

#aktie = TSLA
start = dt.datetime(2020,1,1)
end = dt.datetime(2020,11,30)

df = web.DataReader('GOOG', 'yahoo', start, end)

# df = pd.read_csv('tsla.csv', parse_dates=True, index_col=0)
#df['100ma'] = df['Adj Close'].rolling(window=100, min_periods=0).mean()        # 100 Average
#df['38ma'] = df['Adj Close'].rolling(window=38, min_periods=0).mean()          # 38  Average
 
class Analyse():

    def durchschnitt():
        style.use('ggplot')

        df['100ma'] = df['Adj Close'].rolling(window=100, min_periods=0).mean()        # 100 Average
        df['38ma'] = df['Adj Close'].rolling(window=38, min_periods=0).mean()           # 38  Average
        
        print(df.head())

        ax1 = plt.subplot2grid((6,1), (0,0), rowspan=5, colspan=1)
        ax1.plot(df.index, df['Adj Close'])
        ax1.plot(df.index, df['100ma'])
        ax1.plot(df.index, df['38ma'])   

        plt.show()


    def volumen():
        style.use('ggplot')

        print(df.head())

        ax1 = plt.subplot2grid((6,1), (0,0), rowspan=5, colspan=1)
        ax1.bar(df.index, df['Volume'])

        plt.show()

#def ausgabe():
    #print(df.head())

    #ax1 = plt.subplot2grid((6,1), (0,0), rowspan=5, colspan=1)
    #ax2 = plt.subplot2grid((6,1), (5,0), rowspan=1, colspan=1, sharex=ax1)

    #ax1.plot(df.index, df['Adj Close'])
    #ax1.plot(df.index, df['100ma'])
    #ax1.plot(df.index, df['38ma'])
    #ax2.bar(df.index, df['Volume'])

   # plt.show()

durchschnitt()
#volumen()
#ausgabe()

