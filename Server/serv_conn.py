#!/usr/bin/env python
# -*- coding: utf-8 -*-

from twisted.internet.protocol import Factory, Protocol
from twisted.internet import reactor

import pickle
from uuid import uuid4
HOST, PORT = 'localhost', 5177

class ServerFactory(Factory):
    def __init__(self, gui=None):
        # self.count_users = 0
        # self.users = {}     # Сохраняются все пользоватили которые на сервере
        self.gui = gui
        self.count_users = 0

    def buildProtocol(self, addr):
        # сделать сохранение адресов клиентов
        return ServerProtocol(self, self.gui)

class ServerProtocol(Protocol):
    def __init__(self, factory, gui):
        self.factory = factory
        self.gui = gui
        username = 'username' + str(self.factory.count_users)
        print(username)
        self.factory.count_users += 1
        self.gui.users[username] = self


    def connectionMade(self):
        print("********* Connection made *********")
        # print(type({'type':'info','messege':' You connected to server'}))
        self.sendData({'type': 'info', 'messege': ' You connected to server'})
        self.sendData({'type':'registation'})
        self.factory.count_users += 1


    def connectionLost(self, reason):
        print("*******Connetion lost %s" % reason)

    def dataReceived(self,data):
        #s = data.decode('utf-8')
        #print("Data recieved %s" % s)
        s = pickle.loads(data)
        self.gui.getData(s)

        #self.factory.gs.parseData(s)

    def sendData(self,s):
        print("Send data %s" % s)
        data = pickle.dumps(s, 2)

        self.transport.write(data)

if __name__ == '__main__':
    print ("****Start server.....")
    reactor.listenTCP(PORT, ServerFactory())
    reactor.run()
