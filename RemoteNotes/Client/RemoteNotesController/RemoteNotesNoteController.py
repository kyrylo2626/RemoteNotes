from RemoteNotesView.RemoteNotesAddNoteForm import *
from RemoteNotesView.RemoteNotesShowNoteForm import *
from RemoteNotesModel.RemoteNotesDataModels import *
from RemoteNotesModel.client import *

class NoteController:
	def __init__(self, noteCollController, centralwidget):
		self.add_note_window = AddNoteForm()
		self.add_note_window.setupUi(centralwidget)
		self.add_note_window.pushButton.clicked.connect(self.add_new_note)
		self.show_note_window = ShowNoteForm()
		self.show_note_window.setupUi(centralwidget)
		self.noteCollController = noteCollController
		self.user = noteCollController.user

	def add_new_note(self):
		if not self.user.get_request(request='CHECK', req_object='note',
				data=NoteSignatureData(user_id=self.user.user_id, titlenote=self.add_note_window.lineEdit.text())):
			self.add_note_window.right_title()
			self.user.post_request(request='ADD', req_object='note', data=NoteSignatureData(user_id=self.user.user_id,
																			titlenote=self.add_note_window.lineEdit.text(),
																			textnote=self.add_note_window.textEdit.toPlainText(),
																			image=self.add_note_window.new_photo))

			self.add_note_window.add_note_not_vs()
			self.noteCollController.grid_recall()
		else:
			self.add_note_window.wrong_title()

	def remove_note(self, noteSignatureData, mode=False):
		self.user.post_request(request='REMOVE', req_object='note', data=noteSignatureData)
		if mode:
			self.show_note_window.show_note_not_vs()
		else:
			self.noteCollController.cursor()
			self.noteCollController.note_collection_window.remove_hint()
		self.noteCollController.grid_recall()

	def show_note(self, noteSignatureData):
		self.show_note_window.label_5.setText(noteSignatureData.titlenote)
		self.show_note_window.label_4.setText(noteSignatureData.textnote)

		if str(noteSignatureData.image) == "b'0'":
			self.show_note_window.label.setPixmap(QtGui.QPixmap("images/no_img.png"))
		else:
			self.show_note_window.label.setPixmap(QtGui.QPixmap.fromImage(QtGui.QImage.fromData(noteSignatureData.image)))

		self.show_note_window.pushButton.clicked.connect(lambda: self.remove_note(noteSignatureData, True))
		self.show_note_window.pushButton_2.clicked.connect(lambda: self.edit_note_win(noteSignatureData))

	def edit_note_win(self, noteSignatureData):
		self.show_note_window.show_note_not_vs()
		self.add_note_window.add_note_vs()
		self.add_note_window.edit_mode = True
		self.add_note_window.lineEdit.setText(noteSignatureData.titlenote)
		self.add_note_window.label_3.setText("Edit your note:")
		self.add_note_window.textEdit.setText(noteSignatureData.textnote)
		if str(noteSignatureData.image) == "b'0'":
			self.add_note_window.label.setPixmap(QtGui.QPixmap("images/no_img.png"))
		else:
			self.add_note_window.label.setPixmap(QtGui.QPixmap.fromImage(QtGui.QImage.fromData(noteSignatureData.image)))
		self.add_note_window.pushButton.clicked.disconnect()
		self.add_note_window.pushButton.clicked.connect(lambda: self.edit_note_save(noteSignatureData))

	def edit_note_save(self, noteSignatureData):
		if not self.user.get_request(request='CHECK', req_object='note', data=self.add_note_window.lineEdit.text()) or\
		(self.add_note_window.lineEdit.text() == noteSignatureData.titlenote):
			self.add_note_window.right_title()
			noteSignatureData.titlenote = self.add_note_window.lineEdit.text()
			noteSignatureData.textnote = self.add_note_window.textEdit.toPlainText()
			if self.add_note_window.new_photo == b"0":
				try:
					new_image = noteSignatureData.image
				except AttributeError:
					new_image = 0
			else:
				new_image = self.add_note_window.new_photo
			noteSignatureData.image = new_image
			self.user.post_request(request='EDIT', req_object='note', data=noteSignatureData)
			self.add_note_window.add_note_not_vs()
			self.add_note_window.pushButton.clicked.disconnect()
			self.add_note_window.pushButton.clicked.connect(self.add_new_note)
			self.noteCollController.grid_recall()
		else:
			self.add_note_window.wrong_title()

