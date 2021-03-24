# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 14:40:08 2021

@author: arfao
"""

from PyQt5 import QtCore, QtGui, QtWidgets

from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import (
    FigureCanvasQTAgg,
    NavigationToolbar2QT as NavigationToolbar,
)

import numpy as np


class topLevelWindow(QtWidgets.QMainWindow):
    def __init__(self):

        super().__init__()
        # Create central widget and set layout
        self.centralwidget = QtWidgets.QWidget(self)
        self.setCentralWidget(self.centralwidget)
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)

        # Create display frame, assign to parent layout, and create its own layout
        self.displayFrame = QtWidgets.QFrame(self.centralwidget)
        self.gridLayout.addWidget(self.displayFrame, 1, 0, 1, 1)
        self.verticalLayout_1 = QtWidgets.QVBoxLayout(self.displayFrame)

        # Add MplPlot object to display frame and assign to parent layout
        self.plotWidget = MplPlot()
        self.verticalLayout_1.addWidget(self.plotWidget)

        # Create numbers gram, assign to parent layout, and create its own layout
        self.numFrame = QtWidgets.QFrame(self.centralwidget)
        self.gridLayout.addWidget(self.numFrame, 1, 1, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.numFrame)

        # Add QLineEdits to  numbers frame and assign to parent layout
        self.bottomLeftCornerX = QtWidgets.QLineEdit(self.numFrame)
        self.bottomLeftCornerY = QtWidgets.QLineEdit(self.numFrame)
        self.topRightCornerX = QtWidgets.QLineEdit(self.numFrame)
        self.topRightCornery = QtWidgets.QLineEdit(self.numFrame)
        self.verticalLayout_2.addWidget(self.bottomLeftCornerX)
        self.verticalLayout_2.addWidget(self.bottomLeftCornerY)
        self.verticalLayout_2.addWidget(self.topRightCornerX)
        self.verticalLayout_2.addWidget(self.topRightCornery)

        self.plotWidget.regionUpdated.connect(self.update_le)

    @QtCore.pyqtSlot(QtCore.QRectF)
    def update_le(self, region):
        self.bottomLeftCornerX.setText(str(region.left()))
        self.bottomLeftCornerY.setText(str(region.top()))
        self.topRightCornerX.setText(str(region.right()))
        self.topRightCornery.setText(str(region.bottom()))


class MplPlot(FigureCanvasQTAgg):
    regionUpdated = QtCore.pyqtSignal(QtCore.QRectF)

    def __init__(self, parent=None):
        fig = Figure()
        super(MplPlot, self).__init__(fig)
        self.setParent(parent)
        # Create a figure with axes
        self.ax = self.figure.add_subplot(111)
        self.ax.set_xlim((-100, 100))
        self.ax.set_ylim((-100, 100))
        self.ax.plot([0], [0])

        # Initialize junk values
        self.bottomLeftX = 0
        self.bottomLeftY = 0
        self.topRightX = 0
        self.topRightY = 0
        self.x = 0
        self.y = 0

        # Set moving flag false (determines if mouse is being clicked and dragged inside plot). Set graph snap
        self.moving = False

        # Set up connectivity
        self.cid = self.mpl_connect("button_press_event", self.onclick)
        self.cid = self.mpl_connect("button_release_event", self.onrelease)
        self.cid = self.mpl_connect("motion_notify_event", self.onmotion)

    def onclick(self, event):
        self.bottomLeftX = event.xdata
        self.bottomLeftY = event.ydata
        self.topRightX = event.xdata
        self.topRightY = event.ydata

        self.update_rect()

        self.moving = True

    def onrelease(self, event):
        self.topRightX = event.xdata
        self.topRightY = event.ydata

        self.update_rect()

        self.moving = False

    def onmotion(self, event):
        if not self.moving:
            return

        self.topRightX = event.xdata
        self.topRightY = event.ydata
        self.update_rect()

    def update_rect(self):
        x = np.array(
            [
                self.bottomLeftX,
                self.bottomLeftX,
                self.topRightX,
                self.topRightX,
                self.bottomLeftX,
            ]
        )
        y = np.array(
            [
                self.bottomLeftY,
                self.topRightY,
                self.topRightY,
                self.bottomLeftY,
                self.bottomLeftY,
            ]
        )

        self.ax.lines[0].set_xdata(x)
        self.ax.lines[0].set_ydata(y)

        if any(
            e is None
            for e in [
                self.topRightX,
                self.topRightY,
                self.bottomLeftX,
                self.bottomLeftY,
            ]
        ):
            return

        rect = QtCore.QRectF(
            self.topRightX, self.topRightY, self.bottomLeftX, self.bottomLeftY
        )
        self.regionUpdated.emit(rect)
        self.draw()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    w = topLevelWindow()
    w.show()
    sys.exit(app.exec_())