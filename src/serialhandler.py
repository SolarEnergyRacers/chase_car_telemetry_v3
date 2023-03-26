import queue

import serial
from serial import SerialException

import threading
import time


class SerialHandler(threading.Thread):
    def __init__(self, options):
        super().__init__()

        self.options = options

        self._com = None
        self.com_available = False
        self._connect_serial()

        self.in_queue =  queue.Queue()  # packetized data being received from solar car
        self._in_buffer = []            # raw data received from solar car
        self.out_queue = queue.Queue()  # data that will be sent to solar car

        self.last_beacon = 0.0

    def run(self):
        while True:
            try:
                if self.com_available:
                    if self._com.inWaiting() > 0:
                        input_val = self._com.read(size=10)  # reads until \n by default
                        self._in_buffer.append(input_val)

                    if self.out_queue.qsize() > 0:
                        output_val = self.out_queue.get(block=True)
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

    def input_available(self):
        return self.in_queue.qsize() > 0

    def get_next_input(self):
        if self.input_available():
            return self.in_queue.get()
        else:
            return None

    def add_output(self, out_message):
        self.out_queue.put(out_message)

    def _connect_serial(self):
        try:
            self._com = serial.Serial(self.options["serial"]["com"], self.options["serial"]["baud"])
            self._com.timeout = 25
            self.com_available = True
        except SerialException:
            print("Failed to open Serial Connection")
            self.com_available = False
