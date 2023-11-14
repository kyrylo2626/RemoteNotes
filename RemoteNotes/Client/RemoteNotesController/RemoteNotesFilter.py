from RemoteNotesModel.RemoteNotesDataModels import *
from RemoteNotesModel.client import *

class FilterMode:
    def __init__(self, note_coll, user):
        self.note_control = note_coll
        self.note_coll = note_coll.note_collection_window
        self.user = user

    def buttons_mode(self, data = None):
        if data is None:
            if self.note_coll.filter == "Default":
                notes = self.user.get_request(request='GET', req_object='note').user_notes
            elif self.note_coll.filter == "Name":
                notes = self.show_note_by_name(self.note_coll.lineEdit.text())
            elif self.note_coll.filter == "Date":
                notes = self.show_note_by_date(self.note_coll.dateEdit.dateTime().toString('yyyy-MM-dd'))
        else:
            notes = data

        for i in range(self.note_coll.gridLayout.count()):
            self.note_coll.gridLayout.itemAt(i).widget().close()
        if len(notes) > 9:
            self.note_coll.grid_buttons_on()
        else:
            self.note_coll.grid_buttons_off()
        self.note_control.grid_policy(notes[self.note_coll.button_score-9:self.note_coll.button_score])

    def button_r(self):
        if len(self.user.get_request(request='GET', req_object='note').user_notes) > self.note_coll.button_score:
            self.note_coll.button_score += 9
            self.buttons_mode()

    def button_l(self):
        if self.note_coll.button_score != 9:
            self.note_coll.button_score -= 9
            self.buttons_mode()

    def show_note_by_default(self):
        if self.note_coll.comboBox.currentText() == "Default":
            self.buttons_mode()

    def show_note_by_name(self, name):
        note_by_name = [i for i in self.user.get_request(request='GET', req_object='note').user_notes if name.lower() in i['titlenote'].lower()]
        self.buttons_mode(note_by_name)

    def show_note_by_date(self, date):
        note_by_date = [i for i in self.user.get_request(request='GET', req_object='note').user_notes if str(i['modifytime']).split()[0] == date]
        self.buttons_mode(note_by_date)