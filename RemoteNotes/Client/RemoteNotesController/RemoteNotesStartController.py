from RemoteNotesView.RemoteNotesStartForm import *
from RemoteNotesController.RemoteNotesMainWindowController import *
from RemoteNotesModel.RemoteNotesDataModels import *
from RemoteNotesModel.client import *


class StartController:
    
    def __init__(self):
        self.start_window = StartForm()
        self.start_window.setupUi()
        self.start_window.pushButton.clicked.connect(self.validation_data)
        self.start_window.StartWindow.show()


    def validation_data(self):
        if not self.start_window.lineEdit.text() or not self.start_window.lineEdit_2.text():
            self.start_window.wrong_login()
            self.start_window.label.setText("Login or password field is empty. Please type your user data!")
        else:
            user = Client()
            if user.authentication(UserAccountData(login=self.start_window.lineEdit.text(), password=self.start_window.lineEdit_2.text())):
                self.start_window.StartWindow.close()
                self.main_window = MainWindowController(user)
            else:
                self.start_window.wrong_login()
                self.start_window.label.setText("User " + self.log_err() + " not found. Check your login and password!")


    def log_err(self):
        if len(self.start_window.lineEdit.text()) > 7:
            return f"{self.start_window.lineEdit.text()[:7]}..."
        return self.start_window.lineEdit.text()