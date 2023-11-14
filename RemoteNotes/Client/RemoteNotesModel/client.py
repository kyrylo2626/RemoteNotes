from socket import *
import json, pickle
from RemoteNotesModel.config import ip, port

class Client:

	def __init__(self):
		self.user_id = None
		self.client = socket(AF_INET, SOCK_STREAM)
		self.client.connect((ip, port))


	def authentication(self, data):
		server_answer = self.response()
		if server_answer == "authentication_process":
			self.sender(data)
			server_answer = self.response()
			if server_answer == 'Wrong data!':
				return False
			else:
				self.user_id = server_answer.user_id
				return True
		else:
			self.client.close()
			raise Exception("Something went wrong. Please restart application")



	def sender(self, data):
		try:
			self.client.send(pickle.dumps(data))
		except:
			print('error')


	def response(self):
		try:
			data = pickle.loads(self.client.recv(1048576))
			return data
		except Exception as e:
			print(e)
	

	def get_request(self, request, req_object, data = None):
		try:
			if data is None:
				self.sender({'request': request, 'req_object': req_object})
			else:
				self.sender({'request': request, 'req_object': req_object, 'data': data})

			return self.response()

		except Exception as e:
			print(e)


	def post_request(self, request, req_object = None, data = None):
		if request == 'disconnect':
			self.sender('disconnect')
			self.client.close()
		elif request == 'exit':
			self.sender('disconnect')
			self.client.close()
			exit()
		else:
			try:
				if req_object is None or data is None:
					print('Empty')
				else:
					self.sender({'request': request, 'req_object': req_object, 'data': data})
				return self.response()
			except Exception as e:
				print(e)