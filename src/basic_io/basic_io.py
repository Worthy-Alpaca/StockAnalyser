
import json

class Input():

    def parseJSON(self):
        with open('config.json') as file:
            config = json.load(file)
            self.stock1 = config["aktie1"]
            self.stock2 = config["aktie2"]
            self.startDate = config["datum1"]
            self.endDate = config["datum2"]

    def setFirstStock(self, stock):
        self.stock1 = stock

    def setSecondStock(self, stock):
        self.stock2 = stock

    def setStartDate(self, date):
        parsedate = []
        stringDate = date.split("-")
        for i in stringDate:
            parsedate.append(int(i))
        
        self.startDate = parsedate

    def setEndDate(self, date):
        parsedate = []
        stringDate = date.split("-")
        for i in stringDate:
            parsedate.append(int(i))
        
        self.endDate = parsedate

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
