# Ref : https://www.learnpyqt.com/examples/simple-sales-tax-calculator/
import sys
from decimal import Decimal

from PyQt5 import QtCore, QtGui, QtWidgets, uic


qtCreatorFile = "untitled.ui" # Enter file here.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.calc_tax_button.clicked.connect(self.calculate_tax)

    def calculate_tax(self):
        price = Decimal(self.price_box.text())
        tax = Decimal(self.tax_rate.text())
        if self.operators.currentText() =='+':
            total_price = price  + tax
        elif self.operators.currentText() =='-':    
            total_price = price  - tax
        elif self.operators.currentText() =='*':
            total_price = price  * tax
        elif self.operators.currentText() =='/':    
            total_price = price  / tax    
        total_price_string = "The result is: {:.2f}".format(total_price)
        self.results_output.setText(total_price_string)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())