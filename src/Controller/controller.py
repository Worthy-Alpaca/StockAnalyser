"""
Created on 03.12.2020
@author: Stephan Schumacher

Controller class
NOT NEEDED AT THIS POINT
"""

import sys

sys.path.append("C:/Users/Stephan/source/repos/diwi4/src/basic_io")

from basic_io import Input


class Controller:
    def __init__(self, stock1="", stock2="", startDate="", endDate=""):
        self.stock1 = stock1
        self.stock2 = stock2
        self.startDate = startDate
        self.endDate = endDate

if __name__ == "__main__":
    config = Input()
    config.parseJSON()
    print(config.getStock1())