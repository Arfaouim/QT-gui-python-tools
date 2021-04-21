# ------------------------------------------------------
# ---------------------- plot.py -----------------------
# ------------------------------------------------------
from PyQt5.QtWidgets import*
from PyQt5.uic import loadUi
from PyQt5.QtCore import pyqtSlot
from main import MatplotlibWidget
from matplotlib.backends.backend_qt5agg import (NavigationToolbar2QT as NavigationToolbar)

import numpy as np
import random
import sys     


class Second(QMainWindow,MatplotlibWidget):
    
    def __init__(self,main_class):
        super(Second, self).__init__(main_class)
        
        loadUi("plot_output.ui",self)
        self.addToolBar(NavigationToolbar(self.MplWidget.canvas, self))
        self.plot_graph()
        
    def plot_graph(self):
        self.A = float(self.main_class.A_value.text())
        t = np.linspace(0,1,100)
        
        cosinus_signal = np.cos(self.A*2*np.pi*t)

        self.MplWidget.canvas.axes.clear()
        self.MplWidget.canvas.axes.plot(t, cosinus_signal)
        # self.MplWidget.canvas.axes.plot(t, sinus_signal)
        # self.MplWidget.canvas.axes.legend(('cosinus', 'sinus'),loc='upper right')
        # self.MplWidget.canvas.axes.set_title('Cosinus - Sinus Signal')
        self.MplWidget.canvas.draw()