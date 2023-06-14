import json

import logging as lg
import sys

from PyQt5 import QtWidgets

from serialhandler import SerialHandler
from datahandler import DataHandler
from mainwindow import MainWindow

if __name__ == "__main__":

    # read config file
    with open("src/options.json", "r") as opt_file:
        opt = json.load(opt_file)

    # set console logging level
    if opt["app"]["debug"]:
        lg.root.setLevel(lg.DEBUG)
    else:
        lg.root.setLevel(lg.INFO)

    sh = SerialHandler(opt)
    dh = DataHandler(opt)

    app = QtWidgets.QApplication(sys.argv)
    mw = MainWindow()

    sh.new_input.connect(mw.handle_new_input)
    sh.new_input.connect(dh.handle_new_input)

    sh.update_status.connect(mw.on_update_com)
    mw.send.connect(sh.send)


    mw.show()
    sh.start()
    sys.exit(app.exec_())



