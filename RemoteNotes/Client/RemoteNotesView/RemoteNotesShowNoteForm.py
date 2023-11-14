# -*- coding: utf-8 -*-
from RemoteNotesUIForm import *

class ShowNoteForm(UIForm):
    def setupUi(self, centralwidget):
        self.centralwidget = centralwidget
        self.frame2 = QtWidgets.QFrame(self.centralwidget)
        self.frame2.setVisible(False)
        self.frame2.setGeometry(QtCore.QRect(-50, -50, self.screen_size.width()+100, self.screen_size.height()+100))
        self.frame2.setStyleSheet("background: rgba(48, 48, 48, 0.5);")
        self.frame2.setMouseTracking(True)
        self.frame2.mousePressEvent = self.show_note_not_vs
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setVisible(False)
        self.frame.setGeometry(QtCore.QRect(int(self.screen_size.width()/2)-570, int(self.screen_size.height()/2)-325, 1140, 650))
        with open("stylesheets/note_win_style.qss", "r") as stylesheet_file:
            self.frame.setStyleSheet(stylesheet_file.read())
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.toolButton = QtWidgets.QToolButton(self.frame)
        self.toolButton.setGeometry(QtCore.QRect(1090, 0, 50, 50))
        self.toolButton.clicked.connect(self.show_note_not_vs)
        self.toolButton.setObjectName("toolButton")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(50, 85, 715, 515))
        self.label_4.setStyleSheet("background-color: white;border-radius: 7px;font-size: 12pt;padding: 10px;")
        self.label_4.setWordWrap(True)
        self.label_4.setTextFormat(QtCore.Qt.PlainText)
        self.label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_4.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(790, 85, 300, 50))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(790, 155, 300, 50))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(790, 230, 300, 370))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("images/no_img.png"))
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(False)
        self.new_photo = 0
        self.label.setObjectName("label")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(int(self.screen_size.width()/2)-910, 27, 1040, 40))
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")

        self.toolButton.setText("×")
        self.pushButton.setText("Remove note")
        self.pushButton_2.setText("Edit note")

    def show_note_vs(self):
        self.frame.setVisible(True)
        self.frame2.setVisible(True)

    def show_note_not_vs(self, *args):
        self.frame.setVisible(False)
        self.frame2.setVisible(False)
