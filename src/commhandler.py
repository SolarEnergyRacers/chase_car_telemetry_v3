import threading
from threading import Lock

from PyQt5.QtCore import pyqtSlot

from datainput import *
from PyQt5 import QtGui, QtCore

from src.serialhandler import SerialHandler
from src.datahandler import DataHandler


class CommHandler(QtCore.QThread):
    new_input = QtCore.pyqtSignal(object)
    update_com = QtCore.pyqtSignal(object)

    def __init__(self, opt: dict, sh: SerialHandler, dh: DataHandler):
        QtCore.QThread.__init__(self)

        self.opt = opt
        self.sh = sh  # serial handler
        self.dh = dh  # data handler

        self.open_requests = {}
        self.request_id = 1
        self.uih = None

        self.last_received = "no data"
        self.speed_arrow = "no data"
        self.driver_info = "no data"

    def run(self):

        self.update_com.emit(self.sh.com_available) # updates com available in GUI

        while True:
            if self.sh.in_queue.qsize() > 0:  # handle inputs from solar car
                self.last_received = time.strftime("%H:%M:%S")

                inp = self.sh.in_queue.get()

                self.new_input.emit(inp) # updates GUI

                if len(inp) == 11: # 2 Addr + 8 Data + 1 \n
                    di = CANFrame(self.opt, inp)

                    self.dh.uploadDataInput(di)

            self.msleep(50)
    @pyqtSlot()
    def on_send(self, message):
        self.sh.out_queue.put(message)
