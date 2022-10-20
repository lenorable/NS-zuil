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
    @QtCore.pyqtSlot(result=str)
    def welkscherm(self):
        if usecase == "F":
            code = """
                <div class="div_zuil">
                    <div class="formdiv">
                        <textarea type="text" maxlength="140" placeholder="Feedback max. 140 letters" id="feedback" class="input_feedback"></textarea>
                        <button class="input_naam_box"><textarea type="text" maxlength="8" placeholder="Naam of laat leeg" id="naam" class="input_naam"></textarea></button>
                        <button class="date_time" id="timedisplay"></button>

                        <div class="input_enter"></div><div class="input_enter_back" id="input_enter_back"></div>     <button class="input_enter_overlay" onmouseleave="ns_button('out', 'input_enter_back')" onmouseover="ns_button('in', 'input_enter_back')" onclick="stuur()">verzend</button>
                    </div>
                </div>
            """
            return code
        elif usecase == "M":
            code = """
                <input type="text" maxlength="140" placeholder="feedback Max. 140 letters" id="feedback"></input>
                <input type="text" maxlength="8" placeholder="Naam of laat leeg" id="naam"></input>
                <button onclick="stuur()">zend</button>
            """
            return code
        elif usecase == "S":
            code = """
                <input type="text" maxlength="140" placeholder="feedback Max. 140 letters" id="feedback"></input>
                <input type="text" maxlength="8" placeholder="Naam of laat leeg" id="naam"></input>
                <button onclick="stuur()">zend</button>
            """
            return code
        else:
            return "<h1>Herstart en maak opnieuw een keuze <h1>"


    @QtCore.pyqtSlot(str, str, result=str)
    def sendfeedback(self, feedback, naam):
        print(Zuil.inputs(feedback, naam))
        return "data saved"

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

#if usecase == "F":
#    inputs = Zuil.inputs()
#elif usecase == "M":
#    print("new")
#elif usecase == "S":
#    print("new")

windowM = MainWindow()
windowM.setWindowTitle("")
windowM.setGeometry(0, 0, 400, 300)
#flags = Qt.WindowFlags(QtCore.Qt.Tool | Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
#windowM.setWindowFlags(flags)
windowM.showMaximized()

#start the event loop 
app.exec_()