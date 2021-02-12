"""
Created on 20.01.2020
@author: Stephan Schumacher

Class to controll the calculations
"""

""" Import additional modules """
import os
import sys
from inspect import signature

from parents import Canvas



""" Adding current directory to path """
PACKAGE_PARENT = '../..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

from modules.misc.error import ErrorHandling

class Controller(Canvas):
    def __init__(self, frame, data):
        super().__init__(frame)
        self.data = data
        self.plot = None
        self.plot2 = None
        self.funcargs = []
        self.args = [self.data]

    def calculate(self, function):
        self.function = function
        self.figure.clear()
        sig = signature(self.function)
        for n in sig.parameters:
            self.funcargs.append(n)
        if 'both' in self.funcargs:
            self.twoPlot()
        elif len(self.funcargs) == 3 and self.data.getStock2() == False:
            self.onePlot()
        elif len(self.funcargs) == 3:
            self.twoPlot()
        else:
            self.onePlot()

        try:
            self.function(*tuple(self.args))
        except Exception as e:
            ErrorHandling(self.mainframe).handle(e)
        self.canvas.draw()
        
    def onePlot(self):
        self.plot = self.figure.add_subplot(111)
        self.plot.set_ylabel("Price in USD")
        self.args.append(self.plot)
        if len(self.funcargs) == 3:
            self.args.append(self.plot2)

    def twoPlot(self):
        self.plot = self.figure.add_subplot(211)
        self.plot2 = self.figure.add_subplot(212, sharex=self.plot)
        self.plot.set_ylabel("Price in USD")
        self.plot2.set_ylabel("Price in USD")
        self.args.append(self.plot)
        self.args.append(self.plot2)

    def test(self):
        pass
