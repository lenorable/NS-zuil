import psycopg2
import requests
import random

def get_location():
    gekozen_locaties = ["Den Haag","Utrecht","Zwolle"]
    locatie = gekozen_locaties[random.randint(0,2)]

    return locatie

def get_masseges(locatie):
    connection_string = "host='localhost' dbname='berichten' user='postgres' password='k6LfYEIszD1cOP29qTvx'"
    conn = psycopg2.connect(connection_string)
    cursor = conn.cursor()

    query = "SELECT * FROM bericht;"

    cursor.execute(query)
    saves = cursor.fetchall()
    conn.close()

    for colum in saves:
        #0 = bericht| 1 = datum_tijd | 2 = naam | 3 = locatie | 4 = keuring | 5 = datum_tijd_keuring | 6 = naam_mod | 7 = email_mod
        print(colum[2])

def get_wheater():
    resource_uri = "https://api.openweathermap.org/data/2.5/weather?lat=52.095548&lon=5.078522&appid=f9ea5cbeda7f535d303d0d4876054605&units=metric"
    response = requests.get(resource_uri)
    response_data = response.json()

    weer_from_api = "{};{}".format(str(response_data['main']['temp']),str(response_data['weather'][0]['main']))
    return weer_from_api

def get_faciliteiten(locatie):
    connection_string = "host='localhost' dbname='berichten' user='postgres' password='k6LfYEIszD1cOP29qTvx'"
    conn = psycopg2.connect(connection_string)
    cursor = conn.cursor()

    query = "SELECT ov_bike, elevator, toilet, park_and_ride FROM station_service WHERE station_city = '{}'".format(locatie)

    cursor.execute(query)
    saves = cursor.fetchall()
    conn.close()

    for colum in saves:
        #0 = fiets| 1 = lift | 2 = toilet | 3 = P+R

        fasiliteiten = "{},{},{},{}".format(str(colum[0]), str(colum[1]), str(colum[2]), str(colum[3]))
        return fasiliteiten