import Zuil
import moderatie
import scherm

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
                <id id="id">F</id>
                <div class="div_zuil">
                    <div class="bg_image"></div>
                    <div class="menubar">
                        <div class="nslogo"></div>
                        <button onclick="info()">Info</button>
                        <button onclick="privacy()">Privacy</button>
                        <button onclick="contact()">Contact</button>
                        <button onclick="disclaimer()">Disclaimer</button>
                    </div>
                    <div class="info" id="infodiv">
                        <div class="closebar"><button onclick="closemenu()"></button></div>
                    </div>
                    <div class="privacy" id="privacydiv">
                        <div class="closebar"><button onclick="closemenu()"></button></div>
                    </div>
                    <div class="contact" id="contactdiv">
                        <div class="closebar"><button onclick="closemenu()"></button></div>
                    </div>
                    <div class="disclaimer" id="disclaimerdiv">
                        <div class="closebar"><button onclick="closemenu()"></button></div>
                    </div>

                    <div class="formdiv">
                        <textarea type="text" maxlength="140" placeholder="Feedback max. 140 letters" id="feedback" class="input_feedback"></textarea>
                        <button class="input_naam_box"><textarea type="text" maxlength="8" placeholder="Naam of laat leeg" id="naam" class="input_naam"></textarea></button>
                        <button class="date_time" id="timedisplay"></button>

                        <div class="input_enter"></div><div class="input_enter_back" id="input_enter_back"></div><button class="input_enter_overlay" onmouseleave="ns_button('out', 'input_enter_back')" onmouseover="ns_button('in', 'input_enter_back')" onclick="stuur()">verzend</button>
                    </div>
                </div>
            """
            return code
        elif usecase == "M":
            code = """
                <id id="id">M</id>
                <div class="div_mod">
                    <!-- <div class="bg_image"></div> -->
                    <div class="menubar">
                        <div class="nslogo"></div>
                        <button onclick="info()">Info</button>
                        <button onclick="privacy()">Privacy</button>
                        <button onclick="contact()">Contact</button>
                        <button onclick="disclaimer()">Disclaimer</button>
                    </div>
                    <div class="info" id="infodiv">
                        <div class="closebar"><button onclick="closemenu()"></button></div>
                    </div>
                    <div class="privacy" id="privacydiv">
                        <div class="closebar"><button onclick="closemenu()"></button></div>
                    </div>
                    <div class="contact" id="contactdiv">
                        <div class="closebar"><button onclick="closemenu()"></button></div>
                    </div>
                    <div class="disclaimer" id="disclaimerdiv">
                        <div class="closebar"><button onclick="closemenu()"></button></div>
                    </div>

                    <div class="worddiv">
                        <div class="berichtbubbel" id="berichtbubbel"></div>
                        <div class="keuring_button_div">
                            <button onclick="give_feedback(keuring=0, naam_mod='Admin')"><i class="fa-solid fa-xmark"></i></button>
                            <button onclick="give_feedback(keuring=1, naam_mod='Admin')"><i class="fa-solid fa-check"></i></button>
                        </div>
                    </div>
                </div>
            """
            return code
        elif usecase == "S":
            code = """
                <id id="id">S</id>
                <div class="div_scherm_overlay" id="scherm_overlay">
                    <div class="formdiv">
                        <button class="text">kies uw station</button>
                        <button onclick="scherm_locatie(locatie='Utrecht')">Utrecht</button>
                        <button onclick="scherm_locatie(locatie='Zwolle')">Zwolle</button>
                        <button onclick="scherm_locatie(locatie='Den Haag')">Den Haag</button>
                    </div>
                </div>
                <div class="div_scherm">
                    <div class="bericht_div" id="check"></div>
                    <div class="trein_info_div" id="trein_info_id"></div>
                    <button class="locatie_info" id="locatie_div"></button>
                    <div class="weer_info">
                        <button class="tijd" id="timedisplay"></button>
                        <button class="weer_graden" id="weer_graden_id"></button>
                    </div>
                    <div class="faciliteit_info" id="faciliteit_id"></div>
                </div>
            """
            return code
        else:
            return "<h1>Herstart en maak opnieuw een keuze <h1>"


    @QtCore.pyqtSlot(str, str, result=str)
    def sendfeedback(self, feedback, naam):
        print(Zuil.inputs(feedback, naam))
        return "data saved"

    @QtCore.pyqtSlot(result=str)
    def get_bericht_between(self):
        return moderatie.get_bericht()

    @QtCore.pyqtSlot(int, str, str, result=str)
    def give_feedback(self, keuring, mod_naam, bericht):
        print(str(keuring) + mod_naam + bericht)
        return moderatie.keuring(keuring, mod_naam, bericht)

    @QtCore.pyqtSlot(str, result=str)
    def get_faciliteiten(self, locatie_scherm):
        print(str(scherm.get_faciliteiten(locatie_scherm)))
        return scherm.get_faciliteiten(locatie_scherm)

    @QtCore.pyqtSlot(str, result=list)
    def get_current_trains(self, locatie_scherm):
        print(str(scherm.get_trains(locatie_scherm)))
        return scherm.get_trains(locatie_scherm)

    @QtCore.pyqtSlot(str, result=str)
    def get_current_wheater(self, locatie_scherm):
        print(str(scherm.get_wheater(locatie_scherm)))
        return scherm.get_wheater(locatie_scherm)

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