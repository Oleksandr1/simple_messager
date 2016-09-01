"""class of users for serverside."""


class User():
    """Class User.

    Params: name, passwd,id,contacts, photo,
    data and time of last visite, status 'online'.
    """

    def __init__(self):
        """Init new user."""
        self.name = None
        self.passwd = None
        self.id = None
        self.contacts = {}
        self.photo = None
        self.last_time = None
        self.online = False

    def setPasswd(self, passwd):
        """Set Password."""
        self.passwd = passwd
