from dataclasses import dataclass, field


@dataclass(repr=False)
class UserAccountData:
	user_id: int = field(init=False)
	login: str
	password: str



@dataclass(repr=False)
class UserProfileData:
	user_id: int
	firstname: str
	lastname: str
	dateofbirth: str
	sex: int
	status: int
	nickname: str
	email: str
	image: str
	interests: str



@dataclass(frozen=True, repr=False)
class NotePacketData:
	user_notes: list



@dataclass(repr=False)
class NoteSignatureData:
	user_id: int
	titlenote: str
	image: str
	textnote: str
	time: str = None
	note_id: int = None

