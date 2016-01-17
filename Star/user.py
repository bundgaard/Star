import json


class User():
    def __init__(self, name, username, email):
        self.name = name
        self.username = username
        self.email = email

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, newName):
        self.__name == newName

    def is_authenticated(self):
        return True

    def is_anonymous(self):
        return False

    def __str__(self):
        return "User[name={},username={},email={}]" % (self.name, self.username, self.email)


