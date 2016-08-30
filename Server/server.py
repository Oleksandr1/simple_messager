"""Class for server work with connections."""
from serv_conn import ServerFactory
from twisted.internet import reactor

PORT = 5177


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
        
    def broadcastMessage(self, data):
        """Broadcast message to all online users."""
        print('Broadcast message to all users(unrealized) ')
        # TODO: realise method which send 1 message to all users

if __name__ == '__main__':
    sever = Server()
