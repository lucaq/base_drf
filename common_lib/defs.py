
class LoginParams:
    def __init__(self, username=None, password=None):
        if username is None and password is None:
            raise ValueError()
        self._username = username
        self._password = password

    @property
    def username(self):
        return self._username

    @property
    def password(self):
        return self._password
