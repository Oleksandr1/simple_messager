#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from twisted.internet.protocol import ClientFactory
from twisted.internet.protocol import Protocol

from twisted.internet import reactor
from twisted.internet.task import LoopingCall


HOST, PORT = 'localhost', 5177


# Connection factory for the client
class ClientConnFactory(ClientFactory):
	# Just save the gui on init
	def __init__(self, gui = None):
		self.gui = gui

	# Save the connection, passing it the gs
	def buildProtocol(self, addr):
		print("Build protocol")
		self.addr = addr
		self.conn = ClientConnection(addr, self.gui)
		return self.conn

# Connection for the client
class ClientConnection(Protocol):
	# Save the addr, gui on init
	def __init__(self, addr, gui):
		self.addr = addr
		self.gui = gui

	# On connection, start the game, add the looping call
	# This ensures the game will run indefinitely (at least on twisted's end)
	def connectionMade(self):
		print("connection made")
		self.send('Sanya Connected')

        		#self.gs.sendData("Connected")
#***************** RUN OWN MAIN LOOOP
	#	lc = LoopingCall(self.gui.tick)
	#	lc.start(1/60)
		# When you get data, send it to the gui

	def dataReceived(self, data):
		s = data.decode('utf-8')
		print("GET", s)
		self.gui.GetMessage(s)

	# Send data through the connection
	def send(self, s):
		print("send:", s)
		data = s.encode()
		self.transport.write(data)

	# connection lost
	def connectionLost(self, reason):
		print("lost connection %s" % reason)


def main():
    cf = ClientConnFactory()
    print(HOST, PORT)
    reactor.connectTCP(HOST, PORT, cf)
    reactor.run()

if __name__ == '__main__':
    main()
