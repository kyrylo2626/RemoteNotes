from socket import *
from threading import Thread
import json, pickle

from RemoteNotesModel.RemoteNotesData import *
from config import ip, port


class User:

	def __init__(self, user, user_id):
		self.user = user
		self.user_id = user_id
		

class Server:

	def __init__(self):
		self.active_users = []

		self.server = socket(AF_INET, SOCK_STREAM)
		self.server.bind((ip, port))
		self.server.listen()


	def start_server(self):
		while True:
			user, addr = self.server.accept()
			Thread(target=self.authentication, args=(user, )).start() # async


	def authentication(self, user):
			self.sender(user, 'authentication_process')
			try:
				user_log_data = self.response(user)
			except Exception as e:
				print(e)
				user_log_data = None
				
			if user_log_data is not None:
				if user_log_data == 'disconnect':
					user.close()
				elif userAccountData := Login(user_log_data):
					self.sender(user, userAccountData)
					CurrentUser = User(user, userAccountData.user_id)
					self.active_users.append(CurrentUser)
					self.listen(CurrentUser)
				else:
					self.sender(user, 'Wrong data!')
					user.close()
			else:
				user.close()


	def listen(self, CurrentUser):
		is_work = True
		while is_work:
			try:
				data = self.response(CurrentUser.user)
			except:
				data = ''
				is_work = False

			if data is not None and len(data) > 0:
				if data['request'] == 'disconnect':
					CurrentUser.user.close()
					is_work = False
				else:
					if CurrentUser in self.active_users:
						if data['req_object'] == 'profile':
							self.sender(CurrentUser.user, Profile(CurrentUser.user_id, data))
						elif data['req_object'] == 'note':
							self.sender(CurrentUser.user, Notes(CurrentUser.user_id, data))
						else:
							pass
					else:
						CurrentUser.user.close()
						is_work = False

			else:
				CurrentUser.user.close()
				is_work = False


	def sender(self, user, data):
		try:
			user.send(pickle.dumps(data))
		except Exception as e:
			print(e)


	def response(self, user):
		try:
			return pickle.loads(user.recv(1048576))
		except Exception as e:
			print(e)



	


	


Server().start_server()
