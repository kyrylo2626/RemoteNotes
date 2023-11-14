# -*- coding: utf-8 -*-
from RemoteNotesUIForm import *

class MainWindowForm(UIForm):
    def setupUi(self):
        self.MainWindow.setObjectName("MainWindow")
        self.MainWindow.setWindowTitle("MainWindow")
        self.MainWindow.resize(self.screen_size.width(), self.screen_size.height())
        self.MainWindow.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        with open("stylesheets/main_stylesheet.qss", "r") as stylesheet_file:
            self.MainWindow.setStyleSheet(stylesheet_file.read())
        self.centralwidget = QtWidgets.QWidget(self.MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.MainWindow.setCentralWidget(self.centralwidget)

        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, self.screen_size.width(), 70))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMaximumSize(QtCore.QSize(16777215, 71))
        self.frame.setObjectName("frame")
        self.toolButton = QtWidgets.QToolButton(self.frame)
        self.toolButton.setGeometry(QtCore.QRect(0, 0, 70, 70))
        self.toolButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/three-horizontal-lines-outline-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.toolButton.setIcon(icon)
        self.toolButton.setIconSize(QtCore.QSize(35, 45))
        self.toolButton.clicked.connect(self.menu_bar)
        self.toolButton.setObjectName("toolButton")
        self.label_9 = QtWidgets.QLabel(self.frame)
        self.label_9.setGeometry(QtCore.QRect(int(self.screen_size.width()/2)-65, 15, 130, 40))
        self.label_9.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")
        self.toolButton_2 = QtWidgets.QToolButton(self.frame)
        self.toolButton_2.setGeometry(QtCore.QRect(self.screen_size.width()-60, 0, 60, 70))
        self.toolButton_2.clicked.connect(self.MainWindow.close)
        self.toolButton_2.setObjectName("toolButton_2")
        self.toolButton_3 = QtWidgets.QToolButton(self.frame)
        self.toolButton_3.setGeometry(QtCore.QRect(self.screen_size.width()-80, 0, 20, 70))
        self.toolButton_3.setIconSize(QtCore.QSize(15, 20))
        self.toolButton_3.clicked.connect(self.MainWindow.lower)
        self.toolButton_3.setObjectName("toolButton_3")

        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(0, 70, 230, 240))
        self.groupBox.setTitle("")
        self.groupBox.setFlat(True)
        self.groupBox.setCheckable(False)
        self.groupBox.setChecked(False)
        self.groupBox.setStyleSheet("border: 2px outset rgba(140, 140, 140, 0.2); border-radius: 7px")
        self.groupBox.setVisible(False)
        self.groupBox.setObjectName("groupBox")

        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_3.setGeometry(QtCore.QRect(0, 180, 230, 60))
        self.pushButton_3.clicked.connect(self.MainWindow.close)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_4.setGeometry(QtCore.QRect(0, 120, 230, 60))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_5.setGeometry(QtCore.QRect(0, 60, 230, 60))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_6.setGeometry(QtCore.QRect(0, 0, 230, 60))
        self.pushButton_6.setObjectName("pushButton_6")

        self.label_9.setText("RemoteNotes")
        self.toolButton_2.setText("×")
        self.toolButton_3.setText("—")
        self.pushButton_3.setText("Exit")
        self.pushButton_4.setText("Logout")
        self.pushButton_5.setText("Note Collection")
        self.pushButton_6.setText("Member Profile")

        self.groupBox.leaveEvent = self.hover
        self.pushButton_3.leaveEvent = self.hover
        self.pushButton_4.leaveEvent = self.hover
        self.pushButton_5.leaveEvent = self.hover
        self.pushButton_6.leaveEvent = self.hover

    def menu_bar(self, *args):
        if self.groupBox.isVisible():
            self.groupBox.setVisible(False)
        else:
            self.groupBox.setVisible(True)
            self.menu_bar_raise()

    def menu_bar_raise(self):
        self.frame.raise_()
        self.groupBox.raise_()

    def hover(self, *args):
        if self.groupBox.isVisible():
            if self.centralwidget.cursor().pos().x() > 230 or self.centralwidget.cursor().pos().y() > 310:
                self.menu_bar()
