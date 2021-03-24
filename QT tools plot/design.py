# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 14:37:31 2021

@author: Mehdi Arfaoui
"""

from PyQt5 import QtCore, QtGui, QtWidgets

# **** ADDED THIS
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as Canvas
# **** 

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        #<mainWindow setup stuff>
        self.centralwidget = QtWidgets.QWidget(mainWindow)

        # ****ALTERED THIS FROM self.plotWidget = QtWidgets.QWidget(self.centralWidget)
        self.plotWidget = MplWidget(self.centralWidget)
        # ***** 

        self.plotWidget.setGeometry(QtCore.QRect(20, 250, 821, 591))
        self.plotWidget.setObjectName("plotWidget")

  # **** ADDED THIS 
class MplCanvas(Canvas):
    def __init__(self):
        self.fig = Figure()
        self.ax = self.fig.add_subplot(111)
        Canvas.__init__(self, self.fig)
        Canvas.setSizePolicy(self, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        Canvas.updateGeometry(self)


class MplWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.canvas = MplCanvas()
 # ***********