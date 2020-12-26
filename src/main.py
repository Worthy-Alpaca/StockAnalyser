"""
Created on 05.12.2020
@author: Stephan Schumacher

Interface
"""

""" Importing classes """
from basic_io.basic_io import Input
from Model.analyse import Analyse

""" import config """
import config

""" Importing packages """
# import tkinter
import tkinter as tk
from tkinter import filedialog, ttk
from tkcalendar import Calendar
# import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
from matplotlib import pyplot as plt
# import additional modules
import json
import inspect
class Mainframe:
    def __init__(self):
        self.mainframe = tk.Tk()
        self.mainframe.title("STONKS analysis")
        self.mainframe.geometry("1200x750")

        self.calDate1 = None
        self.calDate2 = None
        self.dateLabel1 = tk.Label(self.mainframe).grid(row=1, column=3)
        self.dateLabel2 = tk.Label(self.mainframe).grid(row=1, column=5)

        self.createMenu()
        self.createButton(8, 0, "Plot", self.plotGraph)
        self.createButton(8, 1, "test", self.donothing)
        self.createForms()
        self.setFigure()
        
    """ @description: method that creates the File menu """
    def createMenu(self):
       menubar = tk.Menu(self.mainframe)
       filemenu = tk.Menu(menubar, tearoff=0)
       filemenu.add_command(label="New", command=self.new)
       filemenu.add_command(label="Load", command=self.open)
       filemenu.add_command(label="Save", command=self.saveAs)
       filemenu.add_command(label="Save as...", command=self.saveAs)
       filemenu.add_command(label="Close", command=self.close)
       filemenu.add_separator()

       filemenu.add_command(label="Exit", command=self.close)
       menubar.add_cascade(label="File", menu=filemenu)

       self.mainframe.config(menu=menubar)

    """ @description: method that creates a button """
    def createButton(self, posX, posY, name, function):
       self.button = tk.Button(
           master=self.mainframe, height=1, width=10, text=name, command=function)
       self.button.grid(row=posY, column=posX, padx=(30, 0))

    def method_finder(self, classname):
        methods = []
        class_methods = dir(classname)
        for m in class_methods:
            if m.startswith('__'):
                continue
            elif m.startswith('parseDate'):
                continue
            else:
                methods.append(m)

        return methods

    """ @description: method that creates the inputs """
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

        functions = Analyse()
        OptionList = self.method_finder(functions)

        self.variable = tk.StringVar(self.mainframe)
        self.variable.set(OptionList[0])

        self.stock1 = tk.Entry(self.mainframe)
        self.stock1.grid(row=0, column=1)
        self.stock2 = tk.Entry(self.mainframe)
        self.stock2.grid(row=1, column=1)
        self.date1 = tk.Button(
            master=self.mainframe, height=1, width=10, text="Select", command=lambda: self.showCal1())
        self.date1.grid(row=0, column=3)
        self.date2 = tk.Button(
            master=self.mainframe, height=1, width=10, text="Select", command=lambda: self.showCal2())
        self.date2.grid(row=0, column=5)
        self.option = tk.OptionMenu(self.mainframe, self.variable, *OptionList)
        self.option.grid(row=0, column=7)

    """ @description: dummy function that does nothing """
    def donothing(self):
        pass

    def showCal1(self):
        self.top = tk.Toplevel(self.mainframe)
        def getDate():
            self.top.withdraw()
            self.calDate1 = self.cal.selection_get()
            self.dateLabel1 = tk.Label(
                self.mainframe, text=self.calDate1).grid(row=1, column=3)

        self.cal = Calendar(self.top,
                   font="Arial 14", selectmode='day',
                   cursor="hand1")
        self.cal.pack(fill="both", expand=True)
        ttk.Button(self.top, text="ok", command=getDate).pack()

    def showCal2(self):
        self.top = tk.Toplevel(self.mainframe)

        def getDate():
            self.top.withdraw()
            self.calDate2 = self.cal2.selection_get()
            self.dateLabel2 = tk.Label(
                self.mainframe, text=self.calDate2).grid(row=1, column=5)

        self.cal2 = Calendar(self.top,
                            font="Arial 14", selectmode='day',
                            cursor="hand1")
        self.cal2.pack(fill="both", expand=True)
        ttk.Button(self.top, text="ok", command=getDate).pack()

    """ @description: read all inputs and return as object """
    def parseInput(self):
        data = Input()
        data.setFirstStock(str(self.stock1.get()))
        data.setSecondStock(str(self.stock2.get()))
        data.setStartDate(str(self.calDate1))
        data.setEndDate(str(self.calDate2))
        return data

    """ @description: function that initiates the calculations """
    def plotGraph(self):
        data = self.parseInput()
        chart = Analyse()
        choice = [self.variable.get().lower()]
        # clearing the subplot
        self.plot.cla() 
        # executing the function dynamically       
        for c in choice:
            getattr(chart, c)(data, self.plot)
        
        # refresh the canvas
        self.canvas.draw()
       
    """ @description: create the chart foundation """
    def setFigure(self):
        self.figure = Figure(figsize=(11.6, 6.5), dpi=100)
        self.canvas = FigureCanvasTkAgg(self.figure, master=self.mainframe)
        self.canvas.draw()
        self.canvas.get_tk_widget().grid(
            row=2, column=0, columnspan=10, rowspan=10, padx=(20, 20))
        self.toolbar = NavigationToolbar2Tk(self.canvas, self.mainframe, pack_toolbar=False)
        self.toolbar.update()
        self.toolbar.grid(
            row=13, column=0, columnspan=10, rowspan=10, padx=(20, 20))
        self.plot = self.figure.add_subplot(111)
        
    """ @description: function to clear all inputs """
    def new(self):
        self.stock1.delete(0, 'end')
        self.stock2.delete(0, 'end')

    """ @description: function to save the current inputs to a JSON """
    def saveAs(self):
        file_opt = options = {}
        options['filetypes'] = [('JSON files', '.json'), ('all files', '.*')]
        options['initialdir'] = config._path + "data"

        filename = filedialog.asksaveasfile(defaultextension=".json", **file_opt)
        if filename is None:  
            return
            
        data = {
            "stock1": str(self.stock1.get()),
            "stock2": str(self.stock2.get()),
            "date1": str(self.calDate1),
            "date2": str(self.calDate2)
        }
        json.dump(data, filename)

    """ @description: function to open an existing JSON and load it to the GUI """
    def open(self):
        filename = filedialog.askopenfilename(initialdir=config._path + "data",
                                              title="Select file", filetypes=(("JSON files", "*.json"), ("all files", "*.*")))
        if filename == None or filename == '':
            return
        with open(filename) as file:
            data = json.load(file)

        self.new()
        self.stock1.insert(0, data["stock1"])
        self.stock2.insert(0, data["stock2"])
        self.calDate1 = data["date1"]
        self.calDate2 = data["date2"]
        self.dateLabel1 = tk.Label(
            self.mainframe, text=self.calDate1).grid(row=1, column=3)

        self.calDate2 = data["date2"]
        self.dateLabel2 = tk.Label(
            self.mainframe, text=self.calDate2).grid(row=1, column=5)

    """ @description: function to close the GUI """
    def close(self):
        self.mainframe.quit()

    """ @description: function to run the GUI """
    def run(self):
        self.mainframe.mainloop()
     

if __name__ == "__main__":
    root = Mainframe()
    root.run()
