import threading
from threading import Lock
from datainput import *
from PyQt5 import QtGui, QtCore

class CommHandler(QtCore.QThread):
    def __init__(self, opt, sh, dh):
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

        while True:
            if self.sh.input_available():  # handle inputs from solar car
                self.last_received = time.strftime("%H:%M:%S")

                l = self.sh.get_next_input()

                if len(l) == 11: # 2 Addr + 8 Data + 1 \n
                    di = CANFrame(self.opt, l)

                    self.dh.uploadDataInput(di)

            for comm in self.uih.out_req:
                self.sh.out_queue.append(comm)

            self.msleep(50)
