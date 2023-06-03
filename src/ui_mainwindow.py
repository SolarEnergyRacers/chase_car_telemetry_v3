from PyQt5.QtCore import QCoreApplication, QMetaObject, QRect
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import *

################################################################################
## Form generated from reading UI file 'mainWindowHISJBu.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        if not mainWindow.objectName():
            mainWindow.setObjectName(u"mainWindow")
        mainWindow.resize(1142, 801)
        self.centralwidget = QWidget(mainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lblCommAvailable = QLabel(self.centralwidget)
        self.lblCommAvailable.setObjectName(u"lblCommAvailable")

        self.horizontalLayout.addWidget(self.lblCommAvailable)

        self.lblLastReceived = QLabel(self.centralwidget)
        self.lblLastReceived.setObjectName(u"lblLastReceived")

        self.horizontalLayout.addWidget(self.lblLastReceived)

        self.btnSave = QPushButton(self.centralwidget)
        self.btnSave.setObjectName(u"btnSave")

        self.horizontalLayout.addWidget(self.btnSave)

        self.horizontalLayout.setStretch(0, 4)
        self.horizontalLayout.setStretch(1, 4)
        self.horizontalLayout.setStretch(2, 1)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.plainTextEdit = QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        font = QFont()
        font.setFamily(u"Consolas")
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setUndoRedoEnabled(False)
        self.plainTextEdit.setReadOnly(True)

        self.verticalLayout.addWidget(self.plainTextEdit)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.leditInput = QLineEdit(self.centralwidget)
        self.leditInput.setObjectName(u"leditInput")

        self.horizontalLayout_2.addWidget(self.leditInput)

        self.cbAddNL = QCheckBox(self.centralwidget)
        self.cbAddNL.setObjectName(u"cbAddNL")
        self.cbAddNL.setChecked(True)

        self.horizontalLayout_2.addWidget(self.cbAddNL)

        self.btnSend = QPushButton(self.centralwidget)
        self.btnSend.setObjectName(u"btnSend")

        self.horizontalLayout_2.addWidget(self.btnSend)

        self.horizontalLayout_2.setStretch(0, 10)
        self.horizontalLayout_2.setStretch(1, 1)
        self.horizontalLayout_2.setStretch(2, 1)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(mainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1142, 21))
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(mainWindow)
        self.statusbar.setObjectName(u"statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)

        QMetaObject.connectSlotsByName(mainWindow)
    # setupUi

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QCoreApplication.translate("mainWindow", u"SER Telemetry", None))
        self.lblCommAvailable.setText(QCoreApplication.translate("mainWindow", u"Comm Available", None))
        self.lblLastReceived.setText(QCoreApplication.translate("mainWindow", u"last Received", None))
        self.btnSave.setText(QCoreApplication.translate("mainWindow", u"save to file", None))
        self.plainTextEdit.setPlainText(QCoreApplication.translate("mainWindow", u"19:05.43  < 0xFE 0xA1 0x32 0x21\n"
"19:06.21  > r:g", None))
        self.cbAddNL.setText(QCoreApplication.translate("mainWindow", u"add \\n", None))
        self.btnSend.setText(QCoreApplication.translate("mainWindow", u"Send", None))
    # retranslateUi

