
# ------------------------------------------------------
# ---------------------- main.py -----------------------
# ------------------------------------------------------
from PyQt5.QtWidgets import*
from PyQt5.uic import loadUi
from PyQt5.QtCore import pyqtSlot

from matplotlib.backends.backend_qt5agg import (NavigationToolbar2QT as NavigationToolbar)

import numpy as np
import random
import sys     
from decimal import Decimal


class MatplotlibWidget(QMainWindow):
    def __init__(self):
        
        QMainWindow.__init__(self)

        loadUi("main.ui",self)
        self.setupUi(self)
        self.setWindowTitle("Exact TCL Methode ")
        self.quit.clicked.connect(self.close)
        
        # connect button to function on_click
        # self.start_job.clicked.connect(self.on_click)
        # self.show()
        self.textboxValue = self.A_value.text()
        self.start_job.clicked.connect(self.on_pushButton_clicked)
        self.start_job.clicked.connect(self.passingInformation)
        self.dialog = Second(parent=self)
        
        # print(textboxValue)
        
    def passingInformation(self):
        self.dialog.input1.setText(self.A_value.text())
        self.dialog.displayInfo()
    
    # @pyqtSlot()
    # def on_click(self):
    #     textboxValue = float(self.A_value.text())
    #     QMessageBox.question(self, 'Message - pythonspot.com', "You typed: " + textboxValue, QMessageBox.Ok, QMessageBox.Ok)
    #     self.A_value.setText("")     
    #     r
    #     # self.pushButton_generate_random_signal.clicked.connect(self.update_graph)

    #     # self.addToolBar(NavigationToolbar(self.MplWidget.canvas, self))

    #     # self.pushButton.clicked.connect(self.on_pushButton_clicked)
    #     # self.dialog = Second(self)
     
    def on_pushButton_clicked(self):
        self.dialog.show()
    def cosinus_signal(self,t):
        return np.exp(Decimal(self.A_value.text())*2*np.pi*t)     
        
class Second(QMainWindow):
    
    def __init__(self,parent):
        super(Second, self).__init__(parent)
        self.parent = parent
        
        loadUi("plot_output.ui",self)
        self.addToolBar(NavigationToolbar(self.MplWidget.canvas, self))
        
        # self.A=self.parent.A_value.text()
        # print(f'{MatplotlibWidget.textboxValue}')
        # MatplotlibWidget.pr(self)

        self.plot_graph()
    def plot_graph(self):
        t = np.linspace(0,1,100) 
        # cosinus_signal = np.cos(2*np.pi*t)

        self.MplWidget.canvas.axes.clear()
        self.MplWidget.canvas.axes.plot(t,MatplotlibWidget.cosinus_signal(self.parent,t))
        self.MplWidget.canvas.draw()
    def displayInfo(self):
        self.show()      
        

app = QApplication([])
window = MatplotlibWidget()
window.show()
app.exec_()

