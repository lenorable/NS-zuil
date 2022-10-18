import Zuil

import sys
import os
from PyQt5 import QtWidgets
from PyQt5 import QtWebEngineWidgets
from PyQt5 import QtCore
from PyQt5 import QtWebChannel
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtWebChannel import *

usecase = ""

class Backend(QtCore.QObject):
    @QtCore.pyqtSlot(str, result=str)
    def getRef(self, x):
        print(usecase)
        return usecase

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        #browser en backend functies inladen
        self.backend = Backend()
        self.view = QWebEngineView()

        #een channel maken
        self.channel = QtWebChannel.QWebChannel(self)
        self.view.page().setWebChannel(self.channel)
        self.channel.registerObject("backend", self.backend)

        #het html script zoeken
        dis = os.getcwd()
        dis = dis + "\index.html"
        dis = dis.replace('\\', '/')

        #de browser dingen toevoegen
        self.view.setUrl(QUrl(dis))
        self.setCentralWidget(self.view)
        self.view.setZoomFactor(1)

app = QApplication(sys.argv)

usecase = input("komt u: Feedback geven ('F'), Moderen ('M'), of een scherm opstarten(S)? ")

if usecase == "F":
    inputs = Zuil.inputs()
elif usecase == "M":
    print("new")
elif usecase == "S":
    print("new")

windowM = MainWindow()
windowM.setWindowTitle("")
windowM.setGeometry(0, 0, 400, 300)
#flags = Qt.WindowFlags(QtCore.Qt.Tool | Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
#windowM.setWindowFlags(flags)
windowM.showMaximized()

#start the event loop 
app.exec_()