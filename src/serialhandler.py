import queue
import logging as lg
import serial
from serial import SerialException

from PyQt5 import QtGui, QtCore
import time


class SerialHandler(QtCore.QThread):
    def __init__(self, opt):
        QtCore.QThread.__init__(self)

        self.opt = opt

        self._com = None
        self.com_available = False
        self._connect_serial()

        self.in_queue =  queue.Queue()  # packetized data being received from solar car
        self._in_buffer = []            # raw data received from solar car
        self.out_queue = queue.Queue()  # data that will be sent to solar car

    def run(self):
        while True:
            try:
                if self.com_available:
                    if self._com.inWaiting() > 0:
                        input_val = self._com.read_until()  # reads until \n by default
                        self._in_buffer.append(input_val)

                    if self.out_queue.qsize() > 0:
                        output_val = self.out_queue.get(block=False)
                        self._com.write(output_val.encode("ascii", "ignore"))

                    time.sleep(0.05)

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

    def _input_available(self):
        return self.in_queue.qsize() > 0

    def read(self):
        if self._input_available():
            return self.in_queue.get()
        else:
            return None

    def send(self, out_message):
        self.out_queue.put(out_message)

    def _connect_serial(self):
        try:
            self._com = serial.Serial(self.options["serial"]["com"], self.options["serial"]["baud"])
            self._com.timeout = 25
            self.com_available = True
        except SerialException:
            lg.warning("Failed to open Serial Connection")
            self.com_available = False
