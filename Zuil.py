# maak random choice of location possible
from datetime import datetime
import random
import psycopg2

def inputs(bericht, gebruiker):
    datum_nu = datetime.today()
    tijd_nu = datetime.now()
    gekozen_locaties = ["Den Haag","Utrecht","Zwolle"]

    tijd = tijd_nu.strftime("%I:%M:%S %p")
    datum = datum_nu.strftime("%Y%m%d")
    locatie = gekozen_locaties[random.randint(0,2)]

    datum_tijd = datum + " " + tijd

    connection_string = "host='localhost' dbname='berichten' user='postgres' password='k6LfYEIszD1cOP29qTvx'"
    conn = psycopg2.connect(connection_string)
    cursor = conn.cursor()

    query = "INSERT INTO bericht VALUES ('{}', '{}','{}','{}');".format(bericht, datum_tijd, gebruiker, locatie)
    print(query)

    cursor.execute(query)
    conn.commit()
    conn.close()    

    return bericht, datum, tijd, gebruiker, locatie