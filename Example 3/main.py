import sys
from decimal import Decimal
from PyQt5 import QtCore, QtGui, QtWidgets, uic
import numpy as np
from matplotlib.backends.backend_qt5agg import (NavigationToolbar2QT as NavigationToolbar)

qtCreatorFile = "untitled.ui" # Enter file here.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        
        self.compute.clicked.connect(self.plot_graph)
        self.addToolBar(NavigationToolbar(self.MplWidget.canvas, self))

        
        
    def plot_graph(self):
        a = float(self.input1.text())
        b = float(self.input_2.text())
        t = np.arange(1,10) 
        cosinus_signal = a*np.exp(-b*t)

        self.MplWidget.canvas.axes.clear()
        self.MplWidget.canvas.axes.plot(t,cosinus_signal)
        self.MplWidget.canvas.draw()

        
 


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())