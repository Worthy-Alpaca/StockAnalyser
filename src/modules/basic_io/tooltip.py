"""
Created on 20.01.2020
@author: Stephan Schumacher

Class to create tooltips
"""

""" Importing tkinter """
import tkinter as tk
import config
import json

class CreateToolTip(object):

    def __init__(self, widget, option):
        self.widget = widget
        self.option = option
        self.widget.bind("<Enter>", self.enter)
        self.widget.bind("<Leave>", self.close)

    def enter(self, event=None):
        self.refresh()
        x = y = 0
        x, y, cx, cy = self.widget.bbox("insert")
        x += self.widget.winfo_rootx() + 25
        y += self.widget.winfo_rooty() + 20
        # creates a toplevel window
        self.tw = tk.Toplevel(self.widget)
        # Leaves only the label and removes the app window
        self.tw.wm_overrideredirect(True)
        self.tw.wm_geometry("+%d+%d" % (x, y))
        label = tk.Text(self.tw, height=5, width=70,
                        background='yellow', relief='solid', borderwidth=1,
                        font=("times", "10", "normal"))
        label.pack(ipadx=1)
        label.insert("end", self.text)

    def refresh(self, event=None):
        with open(config._PATH + "src/assets/tooltips.json") as file:
            data = json.load(file)

        self.text = data["tooltips"][self.option.get().lower()]

    def close(self, event=None):
        if self.tw:
            self.tw.destroy()
