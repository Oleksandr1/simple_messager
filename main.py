#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.uic import loadUiType



app = QApplication(sys.argv)

import qt5reactor
qt5reactor.install()

from client_conn import ClientConnFactory
from twisted.internet import reactor

app.setApplicationName('ChatForAll')
form_class, base_class = loadUiType('main_window.ui')


HOST, PORT = 'localhost', 5177
friends = {'233':'Oleksandr','231':'Aleksey'}

class MainWindow(QDialog, form_class):
    """a."""
    def __init__(self, *args):
        super(MainWindow, self).__init__(*args)
        self.setupUi(self)
        self.cf = ClientConnFactory(self)
        #self.msgView.insertHtml('CONNECTED TO SERVER <br>')
        #self.connectToServer()
        self.usersList.addItem('Sanya')

    def connectToServer(self):
        reactor.connectTCP(HOST, PORT, self.cf)
        reactor.run()

    def SendMessage(self):
        msg = self.msgEdit.text()
        if msg != '':
            try:
                self.msgView.insertHtml('<font color="red">YOU: </font>'+self.msgEdit.text()+'<br>')
                #self.cf.sendMessage(msg.encode('utf-8'))
                self.cf.conn.send({'type':'messege','to':'id','message':self.msgEdit.text()})
            except error:
                self.msgView.insertHtml('I CAN`T SEND MESSAGE!<br>')


        self.msgEdit.clear()


    def GetMessage(self, message):
        self.parseData(message)
       
        #self.msgView.insertHtml(message)
        #self.msgView.insertHtml(message['type'])
   
    def parseData(self, data):
        print('Parse Data')
        print(data)
        if data.get('type') == 'info':
            print('get type ')
            print(data['messege'])
            self.msgView.insertHtml(data['messege']+'<br>')

    def tick(self):
        print(tick)


#  -----------------------------------------------------#
if __name__ == '__main__':
    print("Start app")
    form = MainWindow()
    form.setWindowTitle('Simple messeger')
    form.show()
    form.connectToServer()
    sys.exit(app.exec_())
