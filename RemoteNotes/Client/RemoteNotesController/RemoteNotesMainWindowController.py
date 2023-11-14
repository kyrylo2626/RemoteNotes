from RemoteNotesView.RemoteNotesMainWindowForm import *
from RemoteNotesController import RemoteNotesStartController
from RemoteNotesController.RemoteNotesMemberController import *
from RemoteNotesController.RemoteNotesNoteCollectionController import *
from RemoteNotesModel.client import *

import sys

class MainWindowController:
    def __init__(self, user):
        self.user = user
        self.main_window = MainWindowForm()
        self.member_profile()
        self.menu_buttons()
        self.main_window.MainWindow.show()

    def menu_buttons(self):
        self.main_window.pushButton_4.clicked.connect(self.start_action)
        self.main_window.pushButton_6.clicked.connect(self.member_profile)
        self.main_window.pushButton_5.clicked.connect(self.note_collection)

    def main_window_setup(self):
        self.main_window.setupUi()
        self.menu_buttons()

    def start_action(self):
        self.main_window.MainWindow.close()
        self.start_form = RemoteNotesStartController.StartController()

    def member_profile(self):
        self.main_window_setup()
        self.member_window = MemberController(self.main_window.centralwidget, self.user)

    def note_collection(self):
        self.main_window_setup()
        self.notes_window = NoteCollectionController(self.main_window.centralwidget, self.user)
