from RemoteNotesView.RemoteNotesNoteGridForm import *
from RemoteNotesModel.RemoteNotesDataModels import *
from RemoteNotesModel.client import *

class NoteGridController:
    def __init__(self, note_collection_controller, note):
        self.note_collection_controller = note_collection_controller
        self.noteSignatureData = NoteSignatureData(*list(note.values())[1:6], note['note_id'])
        self.note_grid_form = NoteGridForm()
        self.note_grid_form.setupUi(note_collection_controller.note_collection_window)
        self.note_grid_form.NoteCollectionForm.card_frame.mousePressEvent = self.select_card

        if str(self.noteSignatureData.image) == "b'0'":
            self.note_collection_controller.note_collection_window.label.setPixmap(QtGui.QPixmap("images/no_img.png"))
        else:
            self.note_collection_controller.note_collection_window.label.setPixmap(QtGui.QPixmap.fromImage(QtGui.QImage.fromData(self.noteSignatureData.image)))
        self.note_collection_controller.note_collection_window.date_label.setText("-".join(str(self.noteSignatureData.time)[:10].split("-")[::-1]))
        self.note_collection_controller.note_collection_window.name_label.setText(self.noteSignatureData.titlenote)
        self.note_collection_controller.note_collection_window.text_label.setText(f"{self.noteSignatureData.textnote[:120]} . . .")

    def select_card(self, *args):
        if self.note_collection_controller.note_collection_window.remove_mode:
            self.note_collection_controller.note_collection_window.remove_mode = False
            self.note_collection_controller.note_window.remove_note(self.noteSignatureData)
        else:
            self.note_collection_controller.note_window.show_note_window.show_note_vs()
            self.note_collection_controller.note_window.show_note(self.noteSignatureData)

    def get_card(self):
        return self.note_grid_form.NoteCollectionForm.card_frame
