"""
Created on 23.01.2020
@author: Stephan Schumacher

Class to create and inherit the canvas and figure
"""

""" Importing neccessary classes """
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure


class Canvas(object):
    def __init__(self, frame):
        self.mainframe = frame
        #self.testing = "this is a test"
        self.figure = Figure(figsize=(11.6, 6.5), dpi=100)
        self.canvas = FigureCanvasTkAgg(self.figure, master=self.mainframe)
        self.canvas.draw()
        self.tools()

    def tools(self):
        self.canvas.get_tk_widget().grid(
            row=3, column=0, columnspan=10, rowspan=10, padx=(20, 20))
        self.toolbar = NavigationToolbar2Tk(self.canvas, self.mainframe, pack_toolbar=False)
        self.toolbar.update()
        self.toolbar.grid(
            row=13, column=0, columnspan=10, rowspan=10, padx=(20, 20))

    def clear(self):
        self.figure.clear()
