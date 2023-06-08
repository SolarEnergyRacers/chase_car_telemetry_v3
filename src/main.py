import json
import logging as lg
import sys

from PyQt5 import QtWidgets

from serialhandler import SerialHandler
from commhandler import CommHandler
from datahandler import DataHandler
from mainwindow import MainWindow

if __name__ == "__main__":

    # read config file
    with open("options.json", "r") as opt_file:
        opt = json.load(opt_file)

    # set console logging level
    if opt["app"]["debug"]:
        lg.root.setLevel(lg.DEBUG)
    else:
        lg.root.setLevel(lg.INFO)

    sh = SerialHandler(opt)
    dh = DataHandler(opt)

    ch = CommHandler(opt, sh, dh)
    # CommHandler can take any object that implements run, input_available, get_next_input and add_output in place of sh


    app = QtWidgets.QApplication(sys.argv)

    mw = MainWindow(None)
    mw.show()

    sh.start()
    #ch.start()

    sys.exit(app.exec_())

    #ch.wait()


