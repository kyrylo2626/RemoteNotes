# -*- coding: utf-8 -*-
from RemoteNotesUIForm import *

class AddNoteForm(UIForm):
    def setupUi(self, centralwidget):
        self.centralwidget = centralwidget
        self.frame2 = QtWidgets.QFrame(self.centralwidget)
        self.frame2.setVisible(False)
        self.frame2.setGeometry(QtCore.QRect(-50, -50, self.screen_size.width()+100, self.screen_size.height()+100))
        self.frame2.setStyleSheet("background: rgba(48, 48, 48, 0.5);")
        self.frame2.setMouseTracking(True)
        self.frame2.mousePressEvent = self.add_note_not_vs
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
        self.toolButton.clicked.connect(self.add_note_not_vs)
        self.toolButton.setObjectName("toolButton")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(50, 95, 110, 40))
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(160, 95, 605, 40))
        font = QtGui.QFont()
        font.setFamily("Roboto Condensed")
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.textEdit = QtWidgets.QTextEdit(self.frame)
        self.textEdit.setGeometry(QtCore.QRect(50, 155, 715, 445))
        self.textEdit.setAutoFillBackground(False)
        self.textEdit.setStyleSheet("font-size: 12pt;padding-left: 10px;padding-top: 10px;")
        self.textEdit.setPlaceholderText("")
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(790, 85, 300, 50))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(790, 155, 300, 50))
        self.pushButton_2.clicked.connect(self.choose_file)
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(790, 230, 300, 370))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("images/no_img.png"))
        self.new_photo = b"0"
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(435, 25, 270, 40))
        self.label_3.setObjectName("label_3")

        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(160, 60, 605, 40))
        self.label_4.setStyleSheet("color:red")
        self.label_4.setObjectName("label_2")
        self.label_4.setVisible(False)

        self.toolButton.setText("×")
        self.pushButton.setText("Save note")
        self.pushButton_2.setText("Load image")
        self.label_2.setText("Note title :")
        self.label_3.setText("Add new note to collection :")
        self.label_4.setText("A note with that title already exists! Choose another name")
        self.lineEdit.setPlaceholderText("e.g. Shopping list")
        self.textEdit.setPlaceholderText("Type note text")

    def add_note_vs(self):
        self.frame.setVisible(True)
        self.frame2.setVisible(True)

    def add_note_not_vs(self, *args):
        self.frame.setVisible(False)
        self.frame2.setVisible(False)
        self.clean_data()
        self.right_title()

    def clean_data(self):
        self.lineEdit.setText("")
        self.textEdit.setText("")
        self.label.setPixmap(QtGui.QPixmap("images/no_img.png"))
        self.new_photo = b"0"

    def wrong_title(self):
        self.label_4.setVisible(True)
        self.lineEdit.setStyleSheet("border-bottom: 2px solid red;")

    def right_title(self):
        self.label_4.setVisible(False)
        self.lineEdit.setStyleSheet("border-bottom: 2px solid black;")