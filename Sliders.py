# -------------------------------------------------------------------------------
# Name:             Sliders.py
# Purpose:          Example of using Sliders both verticle and Horizontal
#
# Author:           Jeffreaux
#
# Created:          19Aug24
#
# Required Packages:    PyQt5, PyQt5-Tools
# -------------------------------------------------------------------------------

from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QAction, QSlider, QLabel
from PyQt5 import uic
import sys


class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        # Load the UI file
        uic.loadUi("Sliders_GUI.ui", self)

        # define Widgets
        self.btnExit = self.findChild(QPushButton, "btnExit")

        self.actExit = self.findChild(QAction, "actExit")

        # Define labels that will display slider Value
        self.lblHSlider = self.findChild(QLabel, "lblHSlider")
        self.lblVSlider = self.findChild(QLabel, "lblVSlider")

        # Define the Sliders
        self.hSlider = self.findChild(QSlider, "hSlider")
        self.vSlider = self.findChild(QSlider, "vSlider")

        # Define the actions
        self.btnExit.clicked.connect(self.closeEvent)
        self.actExit.triggered.connect(self.closeEvent)

        # The Signal here is valueChanged
        self.hSlider.valueChanged.connect(self.h_slider_moved)
        self.vSlider.valueChanged.connect(self.v_slider_moved)

        # Show the app
        self.show()

    def h_slider_moved(self):
        h_value = str(self.hSlider.value())  # Gets slider value as an String
        self.lblHSlider.setText(h_value)  # Displays value in label.

    def v_slider_moved(self):
        v_value = self.vSlider.value()  # Gets slider value as an Integer
        self.lblVSlider.setText(str(v_value))  # Displays value in label.  Must be a String
    
    
    def closeEvent(self, *args, **kwargs):
        # print("Program closed Successfully!")
        self.close()


# Initialize the App
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()
