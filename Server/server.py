"""Class for server work with connections."""
from serv_conn import ServerFactory
from twisted.internet import reactor
from uuid import uuid4

import pickle


from user import User
PORT = 5177

# users for testing
friends = {'233':'Oleksandr','231':'Aleksey'}

class Server():
    """Class for organisation server work."""

    def __init__(self):
        """Init new server and run reactor."""
        print ('Start server on %s port ...' % PORT)
        self.users = {}   # save all online users.
        self.serv_factory = ServerFactory(self)

        reactor.listenTCP(PORT, self.serv_factory)
        reactor.run()

    def sendData(self, data):
        """Send data from server to  user."""
        print ('Send data to: zzzz: data: %s (unrealized)' % data)
        # TODO: realize method for sending data to a user

    def getData(self, data):
        """Get data from user."""
        print("Get data form: zzzz data: %s (unrealized)" % data)
        self.parseData(data)
 
    def parseData(self, data):
        """Parse incoming data for processing data"""
        if data.get('type') == 'registation':
            self.sendData({'type':'registration'})

        if data.get('type') == 'new user':
            self.registratNewUser(data)

        if data.get('type') == 'user':
            self.connectUser(data)

        if data.get('type') == 'msg':
            self.parseMessege(data)

    def parseMessege(self,  data):
        pass
        #TODO parsing data and send messege to specific user

    def connectUser(self, data):
        pass
        #TODO parse data and check username and passwd
    
    def registratNewUser(self, data):
        pass 
        #TODO parse id, name, paswd



    def broadcastMessage(self, data):
        """Broadcast message to all online users."""
        print('Broadcast message to all users(unrealized) ')
        # TODO: realise method which send 1 message to all users

if __name__ == '__main__':
    sever = Server()
