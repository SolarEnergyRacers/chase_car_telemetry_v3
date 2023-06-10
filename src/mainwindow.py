from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import pyqtSlot

import logging as lg
from datetime import datetime

from ui_mainwindow import Ui_mainWindow

class MainWindow(QtWidgets.QMainWindow, Ui_mainWindow):
    send = QtCore.pyqtSignal(str)

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent=parent)
        self.setupUi(self)

        #self.btnSend.clicked.connect(lambda: self.on_click_send())
        #self.btnSave.clicked.connect(lambda: self.on_click_save())

        self.btnSend.clicked.connect(self.on_click_send)
        self.btnSave.clicked.connect(self.on_click_save)

        self.plainTextEdit.setPlainText("")


    def on_click_send(self):
        txt = self.leditInput.text()
        if self.cbAddNL:
            txt += chr(13)

        curr_time = datetime.utcnow().strftime('%H:%M:%S.%f')[:-3]
        self.plainTextEdit.appendPlainText(f'{curr_time} >> {txt}')
        self.leditInput.setText('')
        self.send.emit(txt)


    def on_click_save(self):
        print("save!!")
        #todo
        pass

    def handle_new_input(self, data):
        lg.info(f'gui received: {data.hex(" ")}')

        curr_time = datetime.utcnow().strftime('%H:%M:%S.%f')[:-3]
        addr = int.from_bytes(data[0:2], 'big') & 0x7FF

        self.plainTextEdit.appendPlainText(f'{curr_time} << {data.hex(" ")} addr: {hex(addr)}')

    def on_update_com(self, available):
        if available:
            self.lblCommAvailable.setText("COM available: TRUE")
        else:
            self.lblCommAvailable.setText("COM available: FALSE")