"""
Created on 05.12.2020
@author: Stephan Schumacher

Interface
"""

# Dummy stuff
from logging import FileHandler
from basic_io.basic_io import Input
from dummy.charts import DummyCharts

# Importing packages
import tkinter as tk
from tkinter import filedialog, Text
import yfinance as yf
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
from matplotlib import pyplot as plt
import os
import json
class Mainframe:
    def __init__(self):
        # green background
        #self.showStartPage(master)
        self.mainframe = tk.Tk()
        self.mainframe.title("chart analysis tool")
        self.mainframe.geometry("1200x700")

        self.createMenu()
        self.createButtonMenu()
        self.createForms()
        self.setFigure()
        
    def createMenu(self):
       menubar = tk.Menu(self.mainframe)
       filemenu = tk.Menu(menubar, tearoff=0)
       filemenu.add_command(label="New", command=self.new)
       filemenu.add_command(label="Load", command=self.open)
       filemenu.add_command(label="Save", command=self.save)
       filemenu.add_command(label="Save as...", command=self.saveAs)
       filemenu.add_command(label="Close", command=self.close)
       filemenu.add_separator()

       filemenu.add_command(label="Exit", command=self.close)
       menubar.add_cascade(label="File", menu=filemenu)

       self.mainframe.config(menu=menubar)

    def createButtonMenu(self):
       self.button_plot = tk.Button(
           master=self.mainframe, height=1, width=10, text="Plot", command=self.plotGraph)
       self.button_analyze = tk.Button(
           master=self.mainframe, height=1, width=10, text="Analze")
       self.button_predict = tk.Button(
           master=self.mainframe, height=1, width=10, text="Predict")
       self.button_plot.grid(row=0, column=8, padx=(30, 0))
       #self.button_analyze.grid(row=0, column=9, padx=(30, 0))
       #self.button_predict.grid(row=0, column=10, padx=(30, 0))

    def createForms(self):
        self.label1 = tk.Label(
           self.mainframe, text="1. Stock name:").grid(row=0, column=0)
        self.label5 = tk.Label(
            self.mainframe, text="2. Stock name:").grid(row=1, column=0)
        self.label2 = tk.Label(
           self.mainframe, text="Start date:").grid(row=0, column=2)
        self.label3 = tk.Label(
           self.mainframe, text="End date").grid(row=0, column=4)
        self.label4 = tk.Label(
           self.mainframe, text="Plot options").grid(row=0, column=6)

        OptionList = [
            "Chartanalyse"
        ]

        self.variable = tk.StringVar(self.mainframe)
        self.variable.set(OptionList[0])

        self.stock1 = tk.Entry(self.mainframe)
        self.stock1.grid(row=0, column=1)
        self.stock2 = tk.Entry(self.mainframe)
        self.stock2.grid(row=1, column=1)
        self.date1 = tk.Entry(self.mainframe)
        self.date1.grid(row=0, column=3)
        self.date2 = tk.Entry(self.mainframe)
        self.date2.grid(row=0, column=5)
        self.option = tk.OptionMenu(self.mainframe, self.variable, *OptionList)
        self.option.grid(row=0, column=7)

    def donothing(self):
       pass

    def parseInput(self):
        data = Input()
        data.setFirstStock(str(self.stock1.get()))
        data.setSecondStock(str(self.stock2.get()))
        data.setStartDate(str(self.date1.get()))
        data.setEndDate(str(self.date2.get()))
        return data

    def plotGraph(self):
        """
        data = Input()
        data.setFirstStock(str(self.stock1.get()))
        data.setSecondStock(str(self.stock2.get()))
        data.setStartDate(str(self.date1.get()))
        data.setEndDate(str(self.date2.get()))"""
        data = self.parseInput()
        print(data)
        #print(data.getAllData())
        #chart = DummyCharts()
        test = DummyCharts().chart(data, self.figure)
        print(test)
        #self.figure.add_subplot(111).plot(test.index, test['Adj Close'])
        #t = np.arange(0, 3, .01)
        #self.figure.add_subplot(111).plot(t, 2 * np.sin(2 * np.pi * t))
        self.canvas.draw()
        
        #chart = str(self.e1.get())
        #startDate = str(self.e2.get())
        #endDate = str(self.e3.get())
        #print(self.variable.get())
        #data = yf.download(chart, start=startDate, end=endDate)
       
    def setFigure(self):
        self.figure = Figure(figsize=(11.6, 6.5), dpi=100)
        #t = np.arange(0, 3, .01)
        #self.figure.add_subplot(111).plot(t, 2 * np.sin(2 * np.pi * t))
        self.canvas = FigureCanvasTkAgg(self.figure, self.mainframe)
        self.canvas.draw()
        self.canvas.get_tk_widget().grid(
            row=2, column=0, columnspan=10, rowspan=10, padx=(20, 20))

        #self.toolbar = NavigationToolbar2Tk(self.canvas, self.mainframe)
        #self.toolbar.update()
        #self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        
    def new(self):
        self.stock1.delete(0, 'end')
        self.stock2.delete(0, 'end')
        self.date1.delete(0, 'end')
        self.date2.delete(0, 'end')

    def save(self):
        pass

    def saveAs(self):
        file_opt = options = {}
        options['filetypes'] = [('JSON files', '.json'), ('all files', '.*')]
        options['initialdir'] = "C:/Users/Stephan/source/repos/diwi4/data"

        filename = filedialog.asksaveasfile(defaultextension=".json", **file_opt)
        if filename is None:  
            return
            
        config = {
            "stock1": str(self.stock1.get()),
            "stock2": str(self.stock2.get()),
            "date1": str(self.date1.get()),
            "date2": str(self.date2.get())
        }
        json.dump(config, filename)


    def open(self):
        filename = filedialog.askopenfilename(initialdir="C:/Users/Stephan/source/repos/diwi4/data",
                                              title="Select file", filetypes=(("JSON files", "*.json"), ("all files", "*.*")))
        
        with open(filename) as file:
            config = json.load(file)

        self.new()
        self.stock1.insert(0, config["stock1"])
        self.stock2.insert(0, config["stock2"])
        self.date1.insert(0, config["date1"])
        self.date2.insert(0, config["date2"])
        #for con in config:
            #print(config[con])
            #self.con.insert(0, config[f"{con}"])

    def close(self):
        self.mainframe.quit()

    def run(self):
        self.mainframe.mainloop()
     

if __name__ == "__main__":
    root = Mainframe()
    root.run()
