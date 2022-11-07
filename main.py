from email.message import EmailMessage
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
                <div class="div_mod_overlay" id="div_mod_overlay">
                    <div class="log_in_form">
                        <input class="email" type="email" placeholder="email" id="login_email"></input>
                        <input class="wachtwoord" type="password" placeholder="wachtwoord" id="login_ww"></input>
                        <button class="login_button" onclick="login()">Log In</button>
                    </div>
                    <div class="log_in_form_new" id="log_in_new_id">
                        <input class="naam_new_mod" type="text" placeholder="naam" id="new_login_naam" maxlength="8"></input>
                        <input class="email" type="email" placeholder="email" id="new_login_email" maxlength="25"></input>
                        <input class="wachtwoord" type="password" placeholder="wachtwoord" id="new_login_ww" maxlength="25"></input>
                        <button class="make_log_in" onclick="maak_acc()" id="maak_acc">Maak account</button>
                        
                        <!-- <button class="show_pass" onclick="show_new_mod()"><i class="fa-solid fa-eye"></i></button> -->
                        <button class="close" onclick="close_new_mod()">close</button>
                    </div>
                </div>
                <div class="div_mod">
                    <!-- <div class="bg_image"></div> -->
                    <div class="menubar">
                        <div class="nslogo"></div>
                        <!-- <button onclick="all_messges()">All</button> -->
                        <button onclick="log_out()">Log uit</button>
                        <button onclick="make_new()">New Mod</button>
                    </div>
                    <div class="info" id="infodiv">
                        <div class="closebar"><button onclick="closemenu()"></button></div>
                    </div>
                    <div class="privacy" id="privacydiv">5
                        <div class="closebar"><button onclick="closemenu()"></button></div>
                    </div>
                    <div class="contact" id="contactdiv">
                        <div class="closebar"><button onclick="closemenu()"></button></div>
                    </div>
                    <div class="disclaimer" id="disclaimerdiv">
                        <div class="closebar"><button onclick="closemenu()"></button></div>
                    </div>

                    <div class="worddiv">
                        <button class="berichtbubbel" id="berichtbubbel"></button>
                        <div class="keuring_button_div">
                            <button onclick="give_feedback(keuring=0)"><i class="fa-solid fa-xmark"></i></button>
                            <button onclick="give_feedback(keuring=1)"><i class="fa-solid fa-check"></i></button>
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
                    <div class="bericht_div" id="bericht_text_id"></div>
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

    @QtCore.pyqtSlot(str, result=list)
    def get_berichten(self, locatie_scherm):
        print(str(scherm.get_masseges(locatie_scherm)))
        return scherm.get_masseges(locatie_scherm)

    @QtCore.pyqtSlot(str, str, result=str)
    def login_between(self, email, wachtwoord):
        print(str(moderatie.login_mod(email, wachtwoord)))
        return moderatie.login_mod(email, wachtwoord)

    @QtCore.pyqtSlot(str, str, str, result=str)
    def login_new_between(self, naam, wachtwoord, email):
        print(str(moderatie.maak_mod(naam, wachtwoord, email)))
        return moderatie.maak_mod(naam, wachtwoord, email)

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

windowM = MainWindow()
windowM.setWindowTitle("")
windowM.setGeometry(0, 0, 400, 300)
#flags = Qt.WindowFlags(QtCore.Qt.Tool | Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
#windowM.setWindowFlags(flags)
windowM.showMaximized()

#start the event loop 
app.exec_()