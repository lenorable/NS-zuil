import psycopg2
from datetime import datetime

def login_mod(email_mod, wachtwoord_mod):
    connection_string = "host='localhost' dbname='berichten' user='postgres' password='k6LfYEIszD1cOP29qTvx'"
    conn = psycopg2.connect(connection_string)
    cursor = conn.cursor()

    query = "SELECT naam_mod, ww_mod FROM mod WHERE email_mod = '{}';".format(email_mod)

    cursor.execute(query)
    saves = cursor.fetchall()
    conn.close()

    if saves != []:
        wachtwoord = (saves[0][1])
        if wachtwoord_mod == wachtwoord:
            return saves[0][0]

    return False

def get_bericht():
    connection_string = "host='localhost' dbname='berichten' user='postgres' password='k6LfYEIszD1cOP29qTvx'"
    conn = psycopg2.connect(connection_string)
    cursor = conn.cursor()

    query = "SELECT bericht FROM bericht WHERE keuring IS NULL ORDER BY datum_tijd ASC LIMIT 1;"

    cursor.execute(query)
    saves = cursor.fetchall()
    conn.close()

    return saves[0][0]

def keuring(keuring, mod_naam, bericht):
    connection_string = "host='localhost' dbname='berichten' user='postgres' password='k6LfYEIszD1cOP29qTvx'"
    conn = psycopg2.connect(connection_string)
    cursor = conn.cursor()

    datum_nu = datetime.today()
    tijd_nu = datetime.now()
    tijd = tijd_nu.strftime("%I:%M:%S %p")
    datum = datum_nu.strftime("%Y%m%d")

    datum_tijd = datum + " " + tijd

    if keuring == 1:
        query = "UPDATE bericht SET keuring = '1', datum_tijd_keuring = '{}' , naam_mod = '{}' WHERE bericht = '{}';".format(datum_tijd, mod_naam, bericht)
        cursor.execute(query)
        conn.commit()
    elif keuring == 0:
        query = "UPDATE bericht SET keuring = '0', datum_tijd_keuring = '{}' , naam_mod = '{}' WHERE bericht = '{}';".format(datum_tijd, mod_naam, bericht)
        cursor.execute(query)
        conn.commit()

    conn.close()

    return "alright"

def maak_mod(mod_naam, nieuwe_naam, nieuw_ww, nieuw_email):
    connection_string = "host='localhost' dbname='berichten' user='postgres' password='k6LfYEIszD1cOP29qTvx'"
    conn = psycopg2.connect(connection_string)
    cursor = conn.cursor()

    query = "SELECT naam_mod FROM mod;"

    cursor.execute(query)
    saves = cursor.fetchall()
    mods = []

    for items in saves:
        mods.append(items[0])

    if nieuwe_naam not in mods:
        if nieuwe_naam != "" and nieuw_email != "" and nieuw_ww != "":
            query = "INSERT INTO mod VALUES ('{}', '{}', '{}');".format(nieuw_email, nieuw_ww, nieuwe_naam)
            cursor.execute(query)
            conn.commit()
            conn.close()

            return "oke"
        else:
            conn.close()
            return "vul alles in"
    else:
        conn.close()
        return "naam niet berschrikbaar"