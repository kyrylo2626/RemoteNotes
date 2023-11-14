from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDesktopWidget, QApplication

class NoteGridForm:
    def setupUi(self, NoteCollectionForm):
        self.NoteCollectionForm = NoteCollectionForm
        self.NoteCollectionForm.card_frame = QtWidgets.QFrame(self.NoteCollectionForm.centralwidget)
        self.NoteCollectionForm.card_frame.setGeometry(QtCore.QRect(210, 270, 553, 226))
        self.NoteCollectionForm.card_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.NoteCollectionForm.card_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.NoteCollectionForm.card_frame.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.NoteCollectionForm.card_frame.setObjectName("card_frame")

        self.NoteCollectionForm.label = QtWidgets.QLabel(self.NoteCollectionForm.card_frame)
        self.NoteCollectionForm.label.setGeometry(QtCore.QRect(20, 20, 160, 170))
        self.NoteCollectionForm.label.setText("")

        self.NoteCollectionForm.label.setPixmap(QtGui.QPixmap("images/no_img.png"))

        self.NoteCollectionForm.label.setScaledContents(True)
        self.NoteCollectionForm.label.setObjectName("label")

        self.NoteCollectionForm.date_label = QtWidgets.QLabel(self.NoteCollectionForm.card_frame)
        self.NoteCollectionForm.date_label.setGeometry(QtCore.QRect(195, 15, 120, 30))
        font = QtGui.QFont()
        font.setFamily("Roboto Condensed")
        font.setPointSize(12)
        self.NoteCollectionForm.date_label.setFont(font)
        self.NoteCollectionForm.date_label.setStyleSheet("font-size: 12pt;")
        self.NoteCollectionForm.date_label.setObjectName("date_label")

        self.NoteCollectionForm.name_label = QtWidgets.QLabel(self.NoteCollectionForm.card_frame)
        self.NoteCollectionForm.name_label.setGeometry(QtCore.QRect(195, 45, 341, 30))
        self.NoteCollectionForm.name_label.setStyleSheet("font-size: 15pt;color: #3f51b5")
        self.NoteCollectionForm.name_label.setObjectName("name_label")
        
        self.NoteCollectionForm.text_label = QtWidgets.QLabel(self.NoteCollectionForm.card_frame)
        self.NoteCollectionForm.text_label.setGeometry(QtCore.QRect(195, 77, 340, 131))
        self.NoteCollectionForm.text_label.setTextFormat(QtCore.Qt.PlainText)
        self.NoteCollectionForm.text_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.NoteCollectionForm.text_label.setScaledContents(False)
        self.NoteCollectionForm.text_label.setWordWrap(True)
        self.NoteCollectionForm.text_label.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.NoteCollectionForm.text_label.setObjectName("text_label")