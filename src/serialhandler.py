import queue
import logging as lg
import serial
from serial import SerialException

from PyQt5 import QtGui, QtCore
import time


class SerialHandler(QtCore.QThread):
    def __init__(self, opt: dict):
        QtCore.QThread.__init__(self)


        self.opt = opt

        self._com = None
        self.com_available = False
        self._connect_serial()

        self.in_queue =  queue.Queue()  # data being received from solar car
        self.out_queue = queue.Queue()  # data that will be sent to solar car

    def run(self):
        while True:
            try:

                if self.com_available:



                    if self._com.inWaiting() > 0:
                        #input_val = self._com.read_until("\n")  # reads until \n by default
                        input_val = self._com.readline()
                        print("inp:")
                        print(input_val)
                        self.in_queue.put(input_val)

                    if self.out_queue.qsize() > 0:
                        output_val = self.out_queue.get(block=False)
                        self._com.write(output_val.encode("ascii", "ignore"))



                elif not self.com_available:
                    self._connect_serial()
                    time.sleep(1) # wait one second before trying to reconnect to serial port

            except serial.SerialException:
                self._com.close()
                self.com_available = False
                print("SerialException")
            except TypeError:
                self._com.close()
                self.com_available = False
                print("TypeError")

    def read(self):
        if self.in_queue.qsize() > 0:
            return self.in_queue.get()
        else:
            return None

    def send(self, out_message):
        self.out_queue.put(out_message)

    def _connect_serial(self):
        try:
            self._com = serial.Serial(self.opt["serial"]["com"], self.opt["serial"]["baud"])
            self._com.timeout = 25
            self.com_available = True
        except SerialException:
            lg.warning("Failed to open Serial Connection")
            self.com_available = False
