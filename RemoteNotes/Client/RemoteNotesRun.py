import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDesktopWidget, QApplication
from RemoteNotesUIForm import *
from RemoteNotesController.RemoteNotesStartController import *

class Application:
    def __init__(self):
        self.app = QtWidgets.QApplication(sys.argv)
        UIForm.StartWindow = QtWidgets.QMainWindow()
        UIForm.MainWindow = QtWidgets.QMainWindow()
        UIForm.screen_size = QDesktopWidget().availableGeometry()
        self.start_window = StartController()
        sys.exit(self.app.exec_())

    def show_window(self):
        self.MainWindow.show()

app = Application()