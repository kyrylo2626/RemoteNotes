# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDesktopWidget, QApplication

class UIForm:
    StartWindow = None
    MainWindow = None

    def close_window(self):
        self.MainWindow.close()

    # @abstractmethod
    def setupUi(self):
        pass

    def choose_file(self):
        file = QtWidgets.QFileDialog.getOpenFileName(self.MainWindow, caption='Select photo:', filter='Image Files (*.png *.jpg *.bmp)')
        try:
            with open(str(file[0]), 'rb') as file:
                self.new_photo = file.read()
            self.label.setPixmap(QtGui.QPixmap(str(file).split("'")[1]))
        except FileNotFoundError:
            pass 
