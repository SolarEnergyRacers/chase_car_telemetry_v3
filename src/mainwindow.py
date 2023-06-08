from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import pyqtSlot

from ui_mainwindow import Ui_mainWindow

class MainWindow(QtWidgets.QMainWindow, Ui_mainWindow):
    send = QtCore.pyqtSignal(object)

    def __init__(self, ch, parent=None):
        super(MainWindow, self).__init__(parent=parent)
        self.setupUi(self)

        self.ch = ch
        self.btnSend.clicked.connect(lambda: self.on_click_send())
        self.btnSave.clicked.connect(lambda: self.on_click_save())


    @pyqtSlot()
    def on_click_send(self):
        txt = self.leditInput.text()
        if self.cbAddNL:
            txt += '\n'
        #self.ch.out_queue.put(txt)
        print(txt)
        self.plainTextEdit.appendPlainText(txt)
        self.leditInput.setText('')

    @pyqtSlot()
    def on_click_save(self):
        #todo
        pass

    @pyqtSlot()
    def on_new_input(self, data):
        #todo formating
        print('gui received:' + data)
        self.plainTextEdit.appendPlainText(data)

    @pyqtSlot()
    def on_update_com(self, available):
        if available:
            self.lblCommAvailable.setText("COM available: TRUE")
        else:
            self.lblCommAvailable.setText("COM available: FALSE")