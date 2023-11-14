import unittest
from unittest.mock import patch, Mock

import sys
sys.path.append('../Client')
sys.path.append('../Client/RemoteNotesModel')
sys.path.append('../Client/RemoteNotesView')
sys.path.append('../Client/RemoteNotesController')
import client
import RemoteNotesStartController
import RemoteNotesNoteGridController

class TestClient(unittest.TestCase):

	@patch('client.Client.__init__', return_value=None)
	def client_class(self,  client_init):

		mock_client = client.Client()
		mock_client.client = Mock(side_effect=None)

		return mock_client


	def test_authentication(self):

		mock_client = self.client_class()

		mock_client.response = Mock(side_effect='Error')
		with self.assertRaises(Exception): mock_client.authentication('data')
		mock_client.response = Mock(side_effect=['authentication_process', 'user_data'])
		with self.assertRaises(AttributeError): mock_client.authentication('data')
		mock_client.response = Mock(side_effect=['authentication_process', 'Wrong data!'])
		self.assertEqual(False, mock_client.authentication('data'))
		

	def test_post_request(self):

		mock_client = self.client_class()
		mock_client.response = Mock(side_effect='r')

		self.assertEqual(None, mock_client.post_request('disconnect'))
		mock_client.client.close.assert_called_once()
		with self.assertRaises(SystemExit): mock_client.post_request('exit')
		self.assertEqual('r', mock_client.post_request('data', 'data', 'data'))
		


class TestStartController(unittest.TestCase):

	@patch('RemoteNotesStartController.StartController.__init__', return_value=None)
	def start_class(self, start_init):

		mock_start = RemoteNotesStartController.StartController()
		mock_start.start_window = Mock(side_effect=None)

		return mock_start


	def test_validation_data(self):

		mock_start = self.start_class()

		test_data = {
			'login': ['', 'login', ''],
			'password': ['', '', 'password']
		}

		for i in range(3):
			mock_start.start_window.lineEdit.text.return_value = test_data['login'][i]
			mock_start.start_window.lineEdit_2.text.return_value = test_data['password'][i]
			self.assertEqual(None, mock_start.validation_data())
			mock_start.start_window.wrong_login.assert_called()


	def test_log_err(self):

		mock_start = self.start_class()

		mock_start.start_window.lineEdit.text.return_value = '12345678910'
		self.assertEqual('1234567...', mock_start.log_err())
		mock_start.start_window.lineEdit.text.return_value = '1234567'
		self.assertEqual('1234567', mock_start.log_err())



class TestNCollController(unittest.TestCase):

	@patch('RemoteNotesNoteGridController.NoteGridController.__init__', return_value=None)
	def notes_class(self, notes_init):

		mock_notes = RemoteNotesNoteGridController.NoteGridController()
		mock_notes.note_collection_controller = Mock(side_effect=None)
		mock_notes.noteSignatureData = Mock(side_effect=None)

		return mock_notes


	def test_select_card(self):

		mock_notes = self.notes_class()

		mock_notes.note_collection_controller.note_collection_window.remove_mode = True
		self.assertEqual(None, mock_notes.select_card())
		mock_notes.note_collection_controller.note_window.remove_note.assert_called()
		mock_notes.note_collection_controller.note_collection_window.remove_mode = False
		self.assertEqual(None, mock_notes.select_card())
		mock_notes.note_collection_controller.note_window.show_note.assert_called()



if __name__ == '__main__':
	unittest.main()