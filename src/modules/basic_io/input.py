"""
Created on 16.12.2020
@author: Stephan Schumacher

Input Class, used for cleaning and parsing input from GUI
"""

from urllib.request import urlopen
import json
import datetime as dt
try:
    from config import _KEY
except:
    from configDUMMY import _KEY

class Input():

    def parseJSON(self):
        with open('config.json') as file:
            config = json.load(file)
            self.stock1 = config["aktie1"]
            self.stock2 = config["aktie2"]
            self.startDate = config["datum1"]
            self.endDate = config["datum2"]

    def setFirstStock(self, stock):
        self.stock1 = self.parseStock(stock)

    def setSecondStock(self, stock):
        self.stock2 = self.parseStock(stock)

    def setStartDate(self, date):
        self.startDate = self.parseDate(date)

    def setEndDate(self, date):
        self.endDate = self.parseDate(date)

    def parseStock(self, stock):
        if (stock.lower() == "google"):
            stock = "alphabet"

        if stock == "":
            return False

        url = (f"https://financialmodelingprep.com/api/v3/search?query={stock.lower()}&limit=10&exchange=NASDAQ&apikey={_KEY}")
        response = urlopen(url)
        data = response.read().decode("utf-8")
        res = json.loads(data)
        if res != []:
            return res[0]["symbol"]
        else:
            return False

    def parseDate(self, date):
        stringDate = date.split("-")
        
        returnDate = dt.datetime(int(stringDate[0]), int(stringDate[1]), int(stringDate[2]))
        return returnDate
        

    def getStock1(self):
        return self.stock1

    def getStock2(self):
        return self.stock2

    def getStartDate(self):
        return self.startDate

    def getEndDate(self):
        return self.endDate

    def getAllData(self):
        return self.stock1, self.stock2, self.startDate, self.endDate


if __name__ == "__main__":
    test = Input()
    test.setFirstStock("tesla")
    #print(test.getStock1())
    #test.parseStock("tesla")
