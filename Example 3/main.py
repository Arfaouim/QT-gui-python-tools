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
        
        self.comfirm.clicked.connect(self.select_job)
        self.addToolBar(NavigationToolbar(self.MplWidget.canvas, self))    
    def select_job(self):    
        if self.comboBox.currentText()=='1':
            print("select a job 1")
            self.compute.clicked.connect(self.plot_graph_1)
        elif self.comboBox.currentText()=='2':
            print("select a job 2")
            self.compute.clicked.connect(self.plot_graph_2)
        elif self.comboBox.currentText()=='3':
            print("select a job 3")
            self.compute.clicked.connect(self.plot_graph_3)            
        else:
            print("select a job to start")


        
      
        
    def plot_graph_1(self):
        a = float(self.input1.text())
        b = float(self.input_2.text())
        t = np.arange(-10,10) 
        f = a*(t-b)

        self.MplWidget.canvas.axes.clear()
        self.MplWidget.canvas.axes.plot(t,f)
        self.MplWidget.canvas.draw()  
        
    def plot_graph_2(self):
        a = float(self.input1.text())
        b = float(self.input_2.text())
        t = np.arange(-10,10) 
        f = a*np.exp(-b*t)

        self.MplWidget.canvas.axes.clear()
        self.MplWidget.canvas.axes.plot(t,f)
        self.MplWidget.canvas.draw()

    def plot_graph_3(self):
        a = float(self.input1.text())
        b = float(self.input_2.text())
        x = np.arange(-10,10) 
        y = np.arange(-10,10) 
        X, Y = np.meshgrid(x, y)
        f = a*np.exp(-(X**2 + Y**2)/(2*b**2))

        self.MplWidget.canvas.axes.clear()
        self.MplWidget.canvas.axes.contourf(X,Y,f)
        self.MplWidget.canvas.draw()
            
 


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())