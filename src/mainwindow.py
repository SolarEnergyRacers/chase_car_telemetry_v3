from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSlot

from src.commhandler import CommHandler
from ui_mainwindow import Ui_mainWindow

class MainWindow(QtWidgets.QMainWindow, Ui_mainWindow):
    def __init__(self, ch: CommHandler, parent=None):
        super(MainWindow, self).__init__(parent=parent)
        self.setupUi(self)

        self.ch = ch

        self.btnSend.clicked.connect(lambda: self.on_click_send())
        self.btnSave.clicked.connect(lambda: self.on_click_save())
        self.ch.new_input.connect(self.on_new_input)
        self.ch.update_com.connect(self.on_update_com)

    @pyqtSlot()
    def on_click_send(self):
        pass

    @pyqtSlot()
    def on_click_save(self):
        pass

    @pyqtSlot()
    def on_new_input(self, data):
        #todo formating
        self.plainTextEdit.insertPlainText(data)

    @pyqtSlot()
    def on_update_com(self, available):
        if available:
            self.lblCommAvailable.setText("COM available: TRUE")
        else:
            self.lblCommAvailable.setText("COM available: FALSE")