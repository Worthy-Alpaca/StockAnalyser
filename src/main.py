"""
Created on 05.12.2020
@author: Stephan Schumacher

Interface
"""

""" Importing classes """
from modules import Input
from modules import Analyse
from modules import CreateToolTip

""" Importing config """
import config

""" Importing Modules """
import tkinter as tk

""" Importing packages """
from tkinter import filedialog, PhotoImage, ttk
from tkcalendar import Calendar
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
from matplotlib import style

""" Importing additional modules """
import json
import sys
import random
import string
from inspect import signature

class Mainframe:
    def __init__(self):
        self.mainframe = tk.Tk()
        self.mainframe.title("STONKS analysis")
        self.mainframe.geometry("1200x750")
        self.photo = PhotoImage(file = config._path + "src/assets/giphy.gif")
        self.mainframe.iconphoto(True, self.photo)
        """ Declaring things for later use """
        self.calDate1 = None
        self.calDate2 = None
        self.plot = None
        self.plot2 = None
        self.dateLabel1 = tk.Label(self.mainframe).grid(row=1, column=3)
        self.dateLabel2 = tk.Label(self.mainframe).grid(row=1, column=5)
        """ Create UI elements """
        self.createMenu()
        self.createButton(8, 0, "Plot", self.plotGraph)
        self.createButton(8, 1, "Plain Data", self.plainData)
        self.setFigure()
        self.createForms()
        self.tooltip = CreateToolTip(self.option, self.variable)
        
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
    def createButton(self, posX, posY, text, function, margin=None):
        if margin == None:
            margin = 30
        self.button = tk.Button(
            master=self.mainframe, height=1, width=10, text=text, command=function)
        self.button.grid(row=posY, column=posX, padx=(margin, 0))

    """ @description: returns all function names of a given class """
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
           self.mainframe, text="Stock name:").grid(row=0, column=0)
        self.label5 = tk.Label(
            self.mainframe, text="Stock name (optional):").grid(row=1, column=0)
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
        self.option.grid(row=0, column=7, padx=(0, 0))

    """ @description: dummy function that does nothing """
    def donothing(self):
        chart = Analyse()
        choice = self.variable.get().lower()
        method = getattr(chart, choice)
        sig = signature(method)
        print(len(sig.parameters))

    """ @description: display the first calendar """
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

    """ @description: display the second calendar """
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
        if self.stock1.get() == "" or self.calDate1 == None or self.calDate2 == None:
            return None
        data = Input()
        data.setFirstStock(str(self.stock1.get()))
        data.setSecondStock(str(self.stock2.get()))
        data.setStartDate(str(self.calDate1))
        data.setEndDate(str(self.calDate2))
        return data

    """ @description: function that initiates the calculations """
    def plotGraph(self):
        self.figure.clear()
        try:
            data = self.parseInput()
        except Exception as e:
            self.figure.clear()
            return self.errorHandling(e)
        if data == None:
            self.errorHandling("Not enough input")
            return 
        chart = Analyse()
        choice = [self.variable.get()]
        for c in choice:
            method = getattr(chart, c)
            sig = signature(method)
            self.numargs = len(sig.parameters)

        # executing the function dynamically 
        if self.numargs == 3 and data.getStock2() == False:
            self.plot = self.figure.add_subplot(111)
            self.plot2 = None
            self.plot.set_ylabel("Price in USD")
            self.args = (data, self.plot, self.plot2)
        elif self.numargs == 3:
            self.plot = self.figure.add_subplot(211)
            self.plot2 = self.figure.add_subplot(212, sharex=self.plot)
            self.plot.set_ylabel("Price in USD")
            self.plot2.set_ylabel("Price in USD")
            self.args = (data, self.plot, self.plot2)
        else:
            self.plot = self.figure.add_subplot(111)
            self.plot.set_ylabel("Price in USD")
            self.args = (data, self.plot)        

        try:
            for c in choice:
                getattr(chart, c)(*self.args)
        except Exception as e:
            self.figure.clear()
            return self.errorHandling(e)
            
        # refresh the canvas
        self.canvas.draw()

    """ @description: handling errors """
    def errorHandling(self, error):
        self.errorPlot = self.figure.add_subplot(312)
        style.use('ggplot')
        self.errorPlot.axis('off')
        if error == "Not enough input":
            self.errorPlot.set_title(f"Error: {error}", color='C7')
        elif str(error) == "No data fetched for symbol False using YahooDailyReader":
            self.errorPlot.set_title(f"Error: Entered stock could not be found!", color='C7')
        else:
            errorcode = self.errorCode(8)
            with open(config._path + "data/errors.txt", "a") as f:
                f.write(f"{error} : {errorcode}\n")
                f.close()
            self.errorPlot.set_title(f"An error occured. Please report to an application administrator. Errorcode: {errorcode}", color='C7')
        self.canvas.draw()

    """ @description: create an error code """
    def errorCode(self, length):
        letters = string.ascii_lowercase
        result_str = ''.join(random.choice(letters) for i in range(length))
        return result_str

    """ @description: displays just plain data, no calculations """
    def plainData(self):
        data = self.parseInput()
        chart = Analyse()
        # clearing the figure
        self.figure.clear()
        # creating new subplot
        self.plot = self.figure.add_subplot(111)
        self.plot.set_ylabel("Price in USD")
        # executing the function dynamically
        chart.plaindata(data, self.plot)
        # refresh the canvas
        self.canvas.draw()
       
    """ @description: create the chart foundation """
    def setFigure(self):
        self.figure = Figure(figsize=(11.6, 6.5), dpi=100)
        self.canvas = FigureCanvasTkAgg(self.figure, master=self.mainframe)
        self.canvas.draw()
        self.canvas.get_tk_widget().grid(
            row=3, column=0, columnspan=10, rowspan=10, padx=(20, 20))
        self.toolbar = NavigationToolbar2Tk(self.canvas, self.mainframe, pack_toolbar=False)
        self.toolbar.update()
        self.toolbar.grid(
            row=13, column=0, columnspan=10, rowspan=10, padx=(20, 20))
        
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
