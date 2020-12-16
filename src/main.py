"""
Created on 05.12.2020
@author: Stephan Schumacher

Interface
"""

#from Controller.controller import Controller
from basic_io.basic_io import Input
import tkinter as tk
#from tkinter import *

class Main:
    def __init__(self, master):
        # green background
        self.showStartPage(master)
        """
        self.canvas = tk.Canvas(master, height=700, width=700, bg="#263D42")
        self.canvas.pack()
        # white frame
        #self.frame = tk.Frame(master, bg="white")
        #self.frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)
        # content
        self.greeting = tk.Label(self.canvas, text="Welcome to the App")
        self.greeting.config(font=('helvetica', 14))
        self.greeting.pack()
        self.setup = tk.Button(self.canvas, text="Set me up", padx=10, pady=5,
                               fg="white", bg="#263D42", command=lambda: self.showSetupPage(self.canvas))
        self.setup.pack()
        
        self.quit = tk.Button(self.canvas, text="Quit", padx=10,
                              pady=5, fg="white", bg="#263D42", command=master.quit())
        self.quit.pack()"""
        
    def showStartPage(self, root):
        canvas1 = tk.Canvas(root, width=400, height=300 )
        canvas1.pack()

        greeting = tk.Label(root, text="Welcome to the App")
        greeting.config(font=('helvetica', 14))
        canvas1.create_window(200, 140, window=greeting)
        setup = tk.Button(root, text="SETUP", padx=10, pady=5,
                          fg="white", bg="#263D42", command=lambda: self.showSetupPage(root))
        quitBTN = tk.Button(root, text="QUIT", padx=10, pady=5,
                             fg="white", bg="#263D42", command=lambda: root.quit())
        canvas1.create_window(200, 180, window=setup)
        canvas1.create_window(200, 240, window=quitBTN)

    def showSetupPage(self, root):
        ##### clear page #####
        for widget in root.winfo_children():
            widget.destroy()

        ##### setup page #####
        setupcanvas = tk.Canvas(root, width=400, height=300 )
        setupcanvas.pack()
        entry1 = tk.Entry(root)
        label1 = tk.Label(root, text="First input")
        startBTN = tk.Button(root, text="START", padx=10, pady=5, fg="white", bg="#263D42", command=lambda: root.quit())
        setupcanvas.create_window(200, 30, window=label1)
        setupcanvas.create_window(200, 45, window=entry1)
        setupcanvas.create_window(200, 90, window=startBTN)

        

        


if __name__ == "__main__":
    root = tk.Tk()
    app = Main(root)
    root.mainloop()
