from RemoteNotesView.RemoteNotesNoteCollectionForm import *
from RemoteNotesController.RemoteNotesNoteController import *
from RemoteNotesController.RemoteNotesNoteGridController import *
from RemoteNotesController.RemoteNotesFilter import *
from RemoteNotesModel.RemoteNotesDataModels import *
from RemoteNotesModel.client import *

class NoteCollectionController:
	def __init__(self, centralwidget, user):
		self.user = user
		self.note_collection_window = NoteCollectionForm()
		self.note_collection_window.setupUi(centralwidget)
		self.note_window = NoteController(self, centralwidget)
		self.filter_mode = FilterMode(self, user)

		self.note_collection_window.addNoteButton.clicked.connect(self.note_window.add_note_window.add_note_vs)
		self.note_collection_window.removeNoteButton.clicked.connect(self.remove_note_action)

		self.note_collection_window.tri_rButton.clicked.connect(self.filter_mode.button_r)
		self.note_collection_window.tri_lButton.clicked.connect(self.filter_mode.button_l)

		self.note_collection_window.comboBox.activated.connect(self.filter_mode.show_note_by_default)
		self.note_collection_window.nameSearchButton.clicked.connect(lambda: self.filter_mode.show_note_by_name(self.note_collection_window.lineEdit.text()))
		self.note_collection_window.dateSearchButton.clicked.connect(lambda: self.filter_mode.show_note_by_date(self.note_collection_window.dateEdit.dateTime().toString('yyyy-MM-dd')))
		notePacketData = self.user.get_request(request='GET', req_object='note').user_notes
		self.grid_policy(notePacketData)
		if len(notePacketData) > 9:
			self.note_collection_window.grid_buttons_on()

	def grid_policy(self, notePacketData):
		grid_list = [(1, 2), (1, 3), (1, 4), (2, 2), (2, 3), (2, 4), (3, 2), (3, 3), (3, 4)]
		for index, note in zip(grid_list[:len(notePacketData)], notePacketData):
			card_class = NoteGridController(self, note)
			self.note_collection_window.gridLayout.addWidget(card_class.get_card(), *index, 1, 1)
		for index in grid_list[len(notePacketData):]:
			self.note_collection_window.gridLayout.addWidget(self.note_collection_window.add_fall_label(), *index, 1, 1)

	def grid_recall(self):
		for i in range(self.note_collection_window.gridLayout.count()):
			self.note_collection_window.gridLayout.itemAt(i).widget().close()
		notePacketData =  self.user.get_request(request='GET', req_object='note').user_notes
		if len(notePacketData) > 9:
			self.note_collection_window.grid_buttons_on()
		else:
			self.note_collection_window.grid_buttons_off()

		if len(notePacketData) > self.note_collection_window.button_score-9:
			self.grid_policy(notePacketData[self.note_collection_window.button_score-9:self.note_collection_window.button_score])
		else:
			self.note_collection_window.button_score -= 9
			self.grid_policy(notePacketData[self.note_collection_window.button_score-9:self.note_collection_window.button_score])

	def remove_note_action(self):
		self.note_collection_window.remove_hint()
		if self.note_collection_window.remove_mode:
			self.note_collection_window.remove_mode = False
		else:
			self.note_collection_window.remove_mode = True
		self.cursor()

	def cursor(self):
		if self.note_collection_window.remove_mode:
			for i in range(self.note_collection_window.gridLayout.count()):
				if self.note_collection_window.gridLayout.itemAt(i).widget().objectName() == "card_frame":
					self.note_collection_window.gridLayout.itemAt(i).widget().setCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
		else:
			for i in range(self.note_collection_window.gridLayout.count()):
				if self.note_collection_window.gridLayout.itemAt(i).widget().objectName() == "card_frame":
					self.note_collection_window.gridLayout.itemAt(i).widget().setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

