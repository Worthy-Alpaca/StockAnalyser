"""
Tutorials
12.12.2020

Combining all S&P 500 company prices into one DataFrame

(https://pythonprogramming.net/combining-stock-prices-into-one-dataframe-python-programming-for-finance/)

"""

import bs4 as bs
import datetime as dt
import pandas as pd
import os
from pandas_datareader import data as pdr
import pickle
import requests
import yfinance as yf

yf.pdr_override()

def save_sp500_tickers():
    resp = requests.get('http://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
    soup = bs.BeautifulSoup(resp.text, 'lxml')
    table = soup.find('table', {'class': 'wikitable sortable'})
    tickers = []
    for row in table.findAll('tr')[1:]:
        ticker = row.findAll('td')[0].text.replace('.', '-')
        ticker = ticker[:-1]
        tickers.append(ticker)
    with open("sp500tickers.pickle", "wb") as f:
        pickle.dump(tickers, f)
    return tickers


# save_sp500_tickers()
def get_data_from_yahoo(reload_sp500=False):
    if reload_sp500:
        tickers = save_sp500_tickers()
    else:
        with open("sp500tickers.pickle", "rb") as f:
            tickers = pickle.load(f)
    if not os.path.exists('stock_dfs'):
        os.makedirs('stock_dfs')
    start = dt.datetime(2010, 6, 8)
    end = dt.datetime.now()
    for ticker in tickers:
        print(ticker)
        if not os.path.exists('stock_dfs/{}.csv'.format(ticker)):
            df = pdr.get_data_yahoo(ticker, start, end)
            df.reset_index(inplace=True)
            df.set_index("Date", inplace=True)
            df.to_csv('stock_dfs/{}.csv'.format(ticker))
        else:
            print('Already have {}'.format(ticker))

def compile_data():
    with open ("sp500tickers.pickle", "rb") as f:
        tickers = pickle.load(f)
    
    main_df = pd.DataFrame()
    for count, ticker in enumerate(tickers):
        #df = pd.read_csv('stock_dfs/{}.csv'.format(tickers), "r")                                      #versuche das Problem zu finden, wie ich den Path richtig aufrufen kann
        df = pd.read_csv('stock_dfs/{}.csv'.format(ticker), delimiter=r'\s+', encoding="utf-8-sig")     #mit dieser Zeile funktioniert es schon etwas besser
        df.set_index('Date', inplace=True)

        df.rename(columns = {'Adj Close':ticker}, inplace=True)
        df.drop(['Open', 'High', 'Low', 'Close', 'Volume'], 1, inplace=True)

        if main_df.empty:
            main_df = df
        else:
            main_df = main_df.join(df, how='outer')
        if count % 10 ==0:
            print(count)

        
    print(main_df.head())
    main_df.to_csv('sp500_joines_closes.csv')

compile_data()

#C:\Users\Yannic\OneDrive\Dokumente\Technische Hochschule Lübeck\Projekt Digitale Wirtschaft\diwi4\beispiele\Internet Tutorial\stock_dfs