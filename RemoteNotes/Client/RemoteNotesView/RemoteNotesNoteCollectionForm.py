# -*- coding: utf-8 -*-
from RemoteNotesUIForm import *

class NoteCollectionForm(UIForm):
    def setupUi(self, centralwidget):
        self.centralwidget = centralwidget
        self.remove_mode = False
        self.addNoteButton = QtWidgets.QPushButton(self.centralwidget)
        self.addNoteButton.setGeometry(QtCore.QRect(70, 110, 185, 50))
        self.addNoteButton.setObjectName("addNoteButton")
        self.removeNoteButton = QtWidgets.QPushButton(self.centralwidget)
        self.removeNoteButton.setGeometry(QtCore.QRect(295, 110, 185, 50))
        self.removeNoteButton.setObjectName("removeNoteButton")
        self.tri_rButton = QtWidgets.QPushButton(self.centralwidget)
        self.tri_rButton.setVisible(False)
        self.tri_rButton.setGeometry(QtCore.QRect(self.screen_size.width()-120, 110, 50, 50))
        self.tri_rButton.setObjectName("tri_rButton")
        self.tri_rButton.setStyleSheet("font-size: 20pt;padding-left: 2px;")
        self.tri_rButton.setText("▶")
        self.tri_lButton = QtWidgets.QPushButton(self.centralwidget)
        self.tri_lButton.setVisible(False)
        self.tri_lButton.setGeometry(QtCore.QRect(self.screen_size.width()-180, 110, 50, 50))
        self.tri_lButton.setObjectName("tri_lButton")
        self.tri_lButton.setStyleSheet("font-size: 20pt;padding-right: 2px;")
        self.tri_lButton.setText("◀")
        self.button_score = 9

        self.labelRemove = QtWidgets.QLabel(self.centralwidget)
        self.labelRemove.setGeometry(QtCore.QRect(870, 110, 250, 50))
        self.labelRemove.setVisible(False)
        self.labelRemove.setText("Click on note to remove")
        self.labelRemove.setStyleSheet("background: transparent;font-size: 13pt;color:red")
        self.labelRemove.setObjectName("labelRemove")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(520, 110, 85, 50))
        self.label.setText("Filter by:")
        self.label.setStyleSheet("background: transparent;font-size: 13pt;")
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(645, 110, 185, 50))
        self.comboBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.comboBox.setEditable(False)
        self.comboBox.setFrame(True)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("Default")
        self.comboBox.addItem("Name")
        self.comboBox.addItem("Date")
        self.comboBox.activated.connect(self.comboBox_form)
        self.filter = "Default"

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setVisible(False)
        self.lineEdit.setGeometry(QtCore.QRect(870, 110, 350, 50))
        self.lineEdit.setStyleSheet("padding-left: 10px;padding-right: 45px;")
        self.lineEdit.setPlaceholderText("Type name of note")
        self.lineEdit.setObjectName("lineEdit")

        self.nameSearchButton = QtWidgets.QToolButton(self.centralwidget)
        self.nameSearchButton.setVisible(False)
        self.nameSearchButton.setGeometry(QtCore.QRect(1180, 120, 30, 30))
        self.nameSearchButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.nameSearchButton.setStyleSheet("image: url(\'images/search.png\');")
        self.nameSearchButton.setObjectName("nameSearchButton")

        self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit.setVisible(False)
        self.dateEdit.setGeometry(QtCore.QRect(870, 110, 250, 50))
        self.dateEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.dateEdit.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.dateEdit.setAccelerated(False)
        self.dateEdit.setKeyboardTracking(True)
        self.dateEdit.setProperty("showGroupSeparator", False)
        self.dateEdit.setCurrentSectionIndex(0)
        self.dateEdit.setStyleSheet("padding-bottom: -10px;padding-right:35px;")
        self.dateEdit.setObjectName("dateEdit")

        self.dateSearchButton = QtWidgets.QToolButton(self.centralwidget)
        self.dateSearchButton.setVisible(False)
        self.dateSearchButton.setGeometry(QtCore.QRect(1080, 120, 30, 30))
        self.dateSearchButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.dateSearchButton.setStyleSheet("image: url(\'images/search.png\');")
        self.dateSearchButton.setObjectName("dateSearchButton")

        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(40, 180, self.screen_size.width()-80, self.screen_size.height()-220))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(30, 30, 30, 30)
        self.gridLayout.setSpacing(60)
        self.gridLayout.setObjectName("gridLayout")

        self.addNoteButton.setText("Add note")
        self.removeNoteButton.setText("Remove note")
        self.addNoteButton.raise_()
        self.removeNoteButton.raise_()

    def comboBox_form(self):
        if self.comboBox.currentText() == "Default":
            self.filter = "Default"
            self.lineEdit.setVisible(False)
            self.lineEdit.setText("")
            self.nameSearchButton.setVisible(False)
            self.dateEdit.setVisible(False)
            self.dateEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(2000, 1, 1), QtCore.QTime(1, 0, 0)))
            self.dateSearchButton.setVisible(False)
        elif self.comboBox.currentText() == "Name":
            self.filter = "Name"
            self.dateEdit.setVisible(False)
            self.dateEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(2000, 1, 1), QtCore.QTime(1, 0, 0)))
            self.dateSearchButton.setVisible(False)
            self.lineEdit.setVisible(True)
            self.nameSearchButton.setVisible(True)
        elif self.comboBox.currentText() == "Date":
            self.filter = "Date"
            self.lineEdit.setVisible(False)
            self.lineEdit.setText("")
            self.nameSearchButton.setVisible(False)
            self.dateEdit.setVisible(True)
            self.dateSearchButton.setVisible(True)

    def add_fall_label(self):
        self.card_frame = QtWidgets.QFrame(self.centralwidget)
        self.card_frame.setGeometry(QtCore.QRect(210, 270, 553, 226))
        self.card_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.card_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.card_frame.setStyleSheet("background: transparent;")
        self.card_frame.setObjectName("empty_card_frame")
        return self.card_frame

    def grid_buttons_on(self):
        self.tri_rButton.setVisible(True)
        self.tri_lButton.setVisible(True)

    def grid_buttons_off(self):
        self.tri_rButton.setVisible(False)
        self.tri_lButton.setVisible(False)

    def remove_hint(self):
        if not self.labelRemove.isVisible():
            if self.filter == "Default":
                self.labelRemove.setGeometry(QtCore.QRect(870, 110, 250, 50))
            elif self.filter == "Name":
                self.labelRemove.setGeometry(QtCore.QRect(1260, 110, 250, 50))
            else:
                self.labelRemove.setGeometry(QtCore.QRect(1160, 110, 250, 50))
            self.labelRemove.setVisible(True)
        else:
            self.labelRemove.setVisible(False)


