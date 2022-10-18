# maak random choice of location possible
from datetime import datetime
import random

def inputs():
    datum_nu = datetime.today()
    tijd_nu = datetime.now()
    gekozen_locaties = ["Den Haag","Utrecht","Zwolle"]

    tijd = tijd_nu.strftime("%H:%M:%S")
    datum = datum_nu.strftime("%d/%m/%Y")
    bericht = input("laat een boodschap achter: ")
    gebruiker = input("naam of laat leeg: ")
    locatie = gekozen_locaties[random.randint(0,2)]

    return bericht, datum, tijd, gebruiker, locatie