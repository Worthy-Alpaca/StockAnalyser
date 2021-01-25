"""
Created on 22.01.2020
@author: Stephan Schumacher

Class to handle Errors
"""

from canvas import Canvas
import config
from matplotlib import style
import random
import string



class ErrorHandling(Canvas):

    def __init__(self, frame):
        super().__init__(frame)

    def handle(self, error):
        self.figure.clear()
        self.errorPlot = self.figure.add_subplot(312)
        
        style.use('ggplot')
        self.errorPlot.axis('off')

        if error == "Not enough input":
            self.errorPlot.set_title(f"Error: {error}", color='C7')
        elif str(error) == "No data fetched for symbol False using YahooDailyReader":
            self.errorPlot.set_title(f"Error: Entered stock could not be found!", color='C7')
        else:
            errorcode = self.errorCode()
            with open(config._path + "data/errors.txt", "a") as f:
                f.write(f"{error} : {errorcode}\n")
                f.close()
            self.errorPlot.set_title(f"An error occured. Please report to an application administrator. Errorcode: {errorcode}", color='C7')
        self.canvas.draw()

    def errorCode(self, length=8):
        letters = string.ascii_lowercase
        result_str = ''.join(random.choice(letters) for i in range(length))
        return result_str
