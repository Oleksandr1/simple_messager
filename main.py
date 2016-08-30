#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.uic import loadUiType
#import reg_window



app = QApplication(sys.argv)

import qt5reactor
qt5reactor.install()

from client_conn import ClientConnFactory
from twisted.internet import reactor

app.setApplicationName('ChatForAll')
form_class, base_class = loadUiType('main_window.ui')


HOST, PORT = 'localhost', 5177

class MainWindow(QDialog, form_class):
    def __init__(self, *args):
        super(MainWindow, self).__init__(*args)
        self.setupUi(self)
        self.cf = ClientConnFactory(self)
        #self.msgView.insertHtml('CONNECTED TO SERVER <br>')
        #self.connectToServer()

    def connectToServer(self):
        reactor.connectTCP(HOST, PORT, self.cf)
        reactor.run()

    def SendMessage(self):
        msg = self.msgEdit.text()
        if msg != '':
            try:
                self.msgView.insertHtml('<font color="red">YOU: </font>'+self.msgEdit.text()+'<br>')
                #self.cf.sendMessage(msg.encode('utf-8'))
                self.cf.conn.send(msg)
            except error:
                self.msgView.insertHtml('I CAN`T SEND MESSAGE!')


        self.msgEdit.clear()


    def GetMessage(self, message):
        self.msgView.insertHtml(message)

    def tick(self):
        print(tick)

    def __del__(self):
        super.__del__()
        print('Destructor')
        reactor.stop()


#  -----------------------------------------------------#
if __name__ == '__main__':
    print("Start app")
    form = MainWindow()
    form.setWindowTitle('Simple Chat')
    form.show()
    form.connectToServer()
    sys.exit(app.exec_())
