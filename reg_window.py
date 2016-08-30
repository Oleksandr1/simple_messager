#coding: utf8
import sys

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox
from PyQt5.uic import loadUiType


form_class, base_class = loadUiType('reg_window.ui')


class Registration_Dialog(QDialog, form_class):
    def __init__(self, *args):
        super(Registration_Dialog, self).__init__(*args)
        self.setupUi(self)

    def PushButton(self):
        self.data = self.name_edit.text()+self.pass_edit.text()
        self.name_edit.clear()
        self.pass_edit.clear()
        self.name_label.setText(self.data)
        Reg_request()

def Start_reg():
    form = Registration_Dialog()
    form.setWindowTitle('MyQtProj')
    form.show()
    sys.exit(form.exec_())

def Reg_request():
    dil = QMessageBox()
    dil.setText("Hello amigo!")
    dil.setIcon(Warning)
#-----------------------------------------------------#

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setApplicationName('MyQtProj')
    Start_reg()