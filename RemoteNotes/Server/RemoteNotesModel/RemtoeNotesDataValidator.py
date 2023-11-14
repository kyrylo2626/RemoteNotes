import re

class ValidationData:
    login_template = re.compile(r'([A-Za-z0-9]{2,20})')

    name_template = re.compile(r'([A-Za-zА-Яа-я]{2,20})')
    nickname_template = re.compile(r'([A-Za-z0-9.\-_]{2,20})')
    email_template = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+') 
    
    title_template = re.compile(r'([A-Za-z0-9.\-_ ]{2,30})')

    def isValid(self, mode, value):
        if value != "":
            if re.fullmatch(mode, value):
                return 1
            return 0
        return "empty"

    # Login Data
    def login(self, value):
        return self.isValid(self.login_template, value)

    def password(self, value):
        return self.isValid(self.login_template, value)

    # User Profile Data
    def firstname(self, value):
        return self.isValid(self.name_template, value)

    def lastname(self, value):
        return self.isValid(self.name_template, value)

    def dateofbirth(self, value):
        return 1950 <= int(value[:4]) <= 2020

    def nickname(self, value):
        return self.isValid(self.nickname_template, value)

    def email(self, value):
        return self.isValid(self.email_template, value)

    # Note Data
    def note_title(self, value):
        return self.isValid(self.title_template, value)


validator = ValidationData()
print(validator.jj())