from RemoteNotesView.RemoteNotesMemberForm import *
from RemoteNotesModel.RemoteNotesDataModels import *
from RemoteNotesModel.client import *


class MemberController:
	def __init__(self, centralwidget, user):
		self.MemberProfileForm = MemberForm()
		self.MemberProfileForm.setupUi(centralwidget)
		self.userProfileData = user.get_request(request='GET', req_object='profile')
		if self.userProfileData:
			self.member_profile_read()
		self.MemberProfileForm.pushButton.clicked.connect(lambda: self.post_member_data(user))

	def member_profile_read(self):
		self.MemberProfileForm.lineEdit.setText(self.userProfileData.firstname)
		self.MemberProfileForm.lineEdit_2.setText(self.userProfileData.lastname)
		self.MemberProfileForm.lineEdit_4.setText(self.userProfileData.nickname)
		self.MemberProfileForm.lineEdit_5.setText(self.userProfileData.email)
		self.MemberProfileForm.textEdit.setText(self.userProfileData.interests)
		if self.userProfileData.sex == 0:
			self.MemberProfileForm.checkBox.setChecked(True)
		else:
			self.MemberProfileForm.checkBox_2.setChecked(True)
		self.MemberProfileForm.comboBoxStatus.setCurrentIndex(self.userProfileData.status)
		self.MemberProfileForm.dateEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(*list(map(int, str(self.userProfileData.dateofbirth).split("-")))), QtCore.QTime(1, 0, 0)))
		if str(self.userProfileData.image) == "b'0'":
			self.MemberProfileForm.label.setPixmap(QtGui.QPixmap("images/no_img.png"))
		else:
			self.MemberProfileForm.label.setPixmap(QtGui.QPixmap.fromImage(QtGui.QImage.fromData(self.userProfileData.image)))

	def post_member_data(self, user):
		if self.userProfileData:
			user.post_request(request='POST', req_object='profile', data=self.member_profile_new_data(user.user_id))
		else:
			user.post_request(request='CREATE', req_object='profile', data=self.member_profile_new_data(user.user_id))

	def member_profile_new_data(self, usrr_id):
		checkBox = 0 if self.MemberProfileForm.checkBox.isChecked() == True else 1
		if self.MemberProfileForm.new_photo is None:
			try:
				new_image = self.userProfileData.image
			except AttributeError:
				new_image = 0
		else:
			new_image = self.MemberProfileForm.new_photo

		return UserProfileData(user_id = usrr_id,
								firstname = self.MemberProfileForm.lineEdit.text(),
								lastname = self.MemberProfileForm.lineEdit_2.text(),
								dateofbirth = self.MemberProfileForm.dateEdit.dateTime().toString('yyyy-MM-dd'),
								sex = checkBox,
				                status = int(self.MemberProfileForm.comboBoxStatus.currentIndex()),
				                nickname = self.MemberProfileForm.lineEdit_4.text(),
				                email = self.MemberProfileForm.lineEdit_5.text(),
				                image = new_image,
				                interests = self.MemberProfileForm.textEdit.toPlainText())
