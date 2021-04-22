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
        if self.comboBox.currentText()=='plot_G_telda':
            print("select a job 1")
            self.Current_job.setText(f"Computing {self.comboBox.currentText()} ...")
            self.compute.clicked.connect(self.plot_graph_1)
        elif self.comboBox.currentText()=='plot_f_2D':
            print("select a job 2")
            self.compute.clicked.connect(self.plot_f_2D)
        elif self.comboBox.currentText()=='3':
            print("select a job 3")
            self.compute.clicked.connect(self.plot_graph_3)            
        else:
            print("select a job to start")


        
     

            
    def f_2D(self,t):
        """
        correlation function of the spin reservoir = Kernel of memory
    
        Returns
        -------
        None.
    
        """
        #t=t*δ
        c0_ = float(self.c0_.text())
        C_0 = float(self.C_0.text())
        w0 = float(self.w0.text())
        I_0 = float(self.I_0.text())
        A = float(self.A_.text())
        h = float(self.h_.text())
        wk = float(self.wk.text())
        N = float(self.number.text())
        p= float(self.polarization.text())
        nu=A*1e-2
        # result= A**2/(N*hbar)*np.exp(-0.5*(t)**2)*np.exp(1j*A*t*hbar/nu) 
        result= A**2/(4*N)*np.exp(-0.5*(t)**2)*np.exp(1j*A*t/nu) 
        return result
    def plot_f_2D(self):

        t = np.arange(-10,10) 
        self.MplWidget.canvas.axes.clear()
        self.MplWidget.canvas.axes.plot(t,self.f_2D(0.5*t).real,linewidth=3,label=r'$0.5\times\nu $')
        self.MplWidget.canvas.axes.plot(t,self.f_2D(t).real,linewidth=3,label=r'$\nu $')
        self.MplWidget.canvas.axes.plot(t,self.f_2D(2*t).real,linewidth=3,label=r'$2\times\nu $')
        self.MplWidget.canvas.axes.plot(t,self.f_2D(3*t).real,linewidth=3,label=r'$3\times\nu $')
        self.MplWidget.canvas.draw()   


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())