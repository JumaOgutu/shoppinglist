#Object to hold users

class Users(object):

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password