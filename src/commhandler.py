import queue

from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import pyqtSlot

from datainput import *


class CommHandler(QtCore.QThread):
    new_input = QtCore.pyqtSignal(object)
    update_com = QtCore.pyqtSignal(object)

    def __init__(self, opt: dict, sh, dh):
        QtCore.QThread.__init__(self)

        self.opt = opt
        self.sh = sh  # serial handler
        self.dh = dh  # data handler

        self.out_queue = queue.Queue()

    def run(self):

        self.update_com.emit(self.sh.com_available) # updates com available in GUI

        while True:

            if self.sh.in_queue.qsize() > 0:  # handle inputs from solar car
                inp = self.sh.in_queue.get()
                self.new_input.emit(inp) # updates GUI

                if len(inp) == 11: # 2 Addr + 8 Data + 1 \n
                    di = CANFrame(self.opt, inp)

                    self.dh.uploadDataInput(di)

            if self.out_queue.qisze() > 0:
                self.sh.out_queue.put(self.out_queue.get())

            self.msleep(50)
