from config import db_config
from RemoteNotesModel.RemoteNotesDataModels import *
from sqlalchemy import create_engine, Table, MetaData, inspect, exc, Column, Integer, String, Date, DateTime, LargeBinary
from sqlalchemy.ext.declarative import declarative_base  
from sqlalchemy.orm import sessionmaker, relationship 
from sqlalchemy_utils import database_exists, create_database
import datetime



Base = declarative_base()

engine = create_engine(db_config)
if not database_exists(engine.url):
    create_database(engine.url)

meta = MetaData(bind=engine)

session_setup = sessionmaker(bind=engine)
session = session_setup()



try:
	class User(Base):
	    __table__ = Table('user', meta, autoload=True)
except exc.NoSuchTableError:
	class User(Base):  
	    __tablename__ = 'user'  
	    
	    user_id = Column(Integer, primary_key=True)  
	    login = Column(String(25), nullable=False)  
	    password = Column(String(25), nullable=False) 

	Base.metadata.create_all(engine)

	session.add(User(login = 'admin', password = 'password')) 
	session.commit()


try:
	class Member(Base):
	    __table__ = Table('member', meta, autoload=True)
except exc.NoSuchTableError:
	class Member(Base):  
	    __tablename__ = 'member'  
	    
	    member_id = Column(Integer, primary_key=True) 
	    user_id = Column(Integer, nullable=False)
	    firstname = Column(String(25))
	    lastname = Column(String(25))
	    dateofbirth = Column(Date())
	    sex = Column(Integer)
	    status = Column(Integer)
	    nickname = Column(String(25))
	    email = Column(String(50))
	    image = Column(LargeBinary())
	    interests = Column(String(500), nullable=False)
	    createtime = Column(DateTime())
	    modifytime = Column(DateTime())

	Base.metadata.create_all(engine)


try:
	class Note(Base):
	    __table__ = Table('note', meta, autoload=True)
except exc.NoSuchTableError:
	class Note(Base):  
	    __tablename__ = 'note'  
	    
	    note_id = Column(Integer, primary_key=True)  
	    user_id = Column(Integer, nullable=False)
	    titlenote = Column(String(30))
	    image = Column(LargeBinary())
	    textnote = Column(String(1500))
	    modifytime = Column(DateTime())
	    createtime = Column(DateTime())

	Base.metadata.create_all(engine)




def objects_as_dict(obj):
    return [{c.key: getattr(i, c.key) for c in inspect(i).mapper.column_attrs} for i in obj]




class Login:

	def __new__(cls, userAccountData):
		return cls.user_auth(userAccountData)


	@staticmethod
	def user_auth(userAccountData):
		try:
			result = session.query(User).filter(User.login == userAccountData.login, User.password == userAccountData.password)
			if result.count():
				userAccountData.user_id = result[0].user_id
				return userAccountData
			return False
		except Exception as exception:
			print(exception)
			return False



class Profile:

	def __new__(cls, user_id, request):
		if request['request'] == 'GET':
			return cls.get_member_data(user_id)
		elif request['request'] == 'POST':
			return cls.post_member_data(request['data'])
		elif request['request'] == 'CREATE':
			return cls.create_member_data(request['data'])
		else:
			pass


	@staticmethod
	def get_member_data(user_id):
		try:
			result = session.query(Member).filter(Member.user_id == user_id)
			if result.count():
				return UserProfileData(user_id = result[0].user_id,
		        						firstname = result[0].firstname,
										lastname = result[0].lastname,
										dateofbirth = result[0].dateofbirth,
										sex = result[0].sex,
						                status = result[0].status,
						                nickname = result[0].nickname,
						                email = result[0].email,
						                image = result[0].image,
						                interests = result[0].interests)
			return False
		except Exception as exception:
			print(exception)
			return False


	@staticmethod
	def post_member_data(userProfileData):
		try:
			result = session.query(Member).filter(Member.user_id == userProfileData.user_id)
			result.update({"firstname": userProfileData.firstname,
							"lastname": userProfileData.lastname,
							"dateofbirth": userProfileData.dateofbirth,
							"sex": userProfileData.sex,
			                "status": userProfileData.status,
			                "nickname": userProfileData.nickname,
			                "email": userProfileData.email,
			                "image": userProfileData.image,
			                "interests": userProfileData.interests,
			                "modifytime": datetime.datetime.now()})
			session.commit()
			return True
		except Exception as exception:
			print(exception)
			return False


	@staticmethod
	def create_member_data(userProfileData):
		try:
			new_member = Member(user_id = userProfileData.user_id,
								firstname = userProfileData.firstname,
								lastname = userProfileData.lastname,
								dateofbirth = userProfileData.dateofbirth,
								sex = userProfileData.sex,
		                        status = userProfileData.status,
		                        nickname = userProfileData.nickname,
		                        email = userProfileData.email,
		                        image = userProfileData.image,
		                        interests = userProfileData.interests,
		                        createtime = datetime.datetime.now(),
		                        modifytime = datetime.datetime.now())
			session.add(new_member) 
			session.commit()
			return True
		except Exception as exception:
			print(exception)
			return False



class Notes:

	def __new__(cls, user_id, request):
		if request['request'] == 'GET':
			return cls.get_notes_list(user_id)
		elif request['request'] == 'ADD':
			return cls.add_note(request['data'])
		elif request['request'] == 'REMOVE':
			return cls.remove_note(request['data'])
		elif request['request'] == 'EDIT':
			return cls.edit_note(request['data'])
		elif request['request'] == 'CHECK':
			return cls.check_note(request['data'])
		else:
			pass


	@staticmethod
	def get_notes_list(user_id):
		try:
			result = session.query(Note).filter(Note.user_id == user_id)
			return NotePacketData(objects_as_dict(result))
		except Exception as exception:
			print(exception)
			return False


	@staticmethod
	def add_note(noteSignatureData):
		try:
			new_note = Note(user_id = noteSignatureData.user_id,
							titlenote = noteSignatureData.titlenote,
							image = noteSignatureData.image,
							textnote = noteSignatureData.textnote,
							modifytime = datetime.datetime.now(),
		                    createtime = datetime.datetime.now()) 
			session.add(new_note) 
			session.commit()
			return True
		except Exception as exception:
			print(exception)
			return False


	@staticmethod
	def remove_note(noteSignatureData):
		try:
			result = session.query(Note).filter(Note.user_id == noteSignatureData.user_id, Note.titlenote == noteSignatureData.titlenote)
			result.delete()
			session.commit()
			return True
		except Exception as exception:
			print(exception)
			return False


	@staticmethod
	def edit_note(noteSignatureData):
		try:
			result = session.query(Note).filter(Note.note_id == noteSignatureData.note_id, Note.user_id == noteSignatureData.user_id)
			result.update({"titlenote": noteSignatureData.titlenote,
							"image": noteSignatureData.image,
							"textnote": noteSignatureData.textnote,
							"modifytime": datetime.datetime.now()})
			session.commit()
			return True
		except Exception as exception:
			print(exception)
			return False


	@staticmethod
	def check_note(noteSignatureData):
		try:
			result = session.query(Note).filter(Note.user_id == noteSignatureData.user_id, Note.titlenote == noteSignatureData.titlenote)
			return result.count()
		except Exception as exception:
			print(exception)
			return False