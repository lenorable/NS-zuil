# maak random choice of location possible
from datetime import datetime
import random
from turtle import ht
import psycopg2


from asyncio.windows_events import NULL
from re import A
from flask import Flask, json, request
from cryptography.fernet import Fernet

api = Flask(__name__)

def locatie_fun():
    gekozen_locaties = ["Den Haag","Utrecht","Zwolle"]
    locatie = gekozen_locaties[random.randint(0,2)]

    return locatie

def inputs(bericht, locatie, gebruiker):
    datum_nu = datetime.today()
    tijd_nu = datetime.now()

    tijd = tijd_nu.strftime("%I:%M:%S %p")
    datum = datum_nu.strftime("%Y%m%d")

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

@api.route('/', methods=['GET', 'POST'])
def get_companies():
    gebruiker = str(request.args.get('gebruiker'))
    bericht = str(request.args.get('bericht'))
    locatie = str(request.args.get('locatie'))
    if bericht != 'None':
        if gebruiker == 'None':
            inputs(bericht, locatie, gebruiker="")
        else:
            inputs(bericht, locatie, gebruiker)

    locatie_from_fun = locatie_fun()

    html = """
            <html>
            <style>
                .form{
                    background-color: rgba(255, 201, 23, 1);
                    width: 100%;
                    height: 100%;
                    position: absolute;
                    left: 0%;
                    top: 0%;
                    border-radius: none;
                    z-index: 1;
                    overflow: hidden;
                    border: none;
                    outline: none;
                    padding: none;
                    margin: 0px;
                    text-align: center;
                    font-size: 2vh;
                }

                .naam{
                    background-color: rgba(255, 255, 255, 1);
                    width: 80%;
                    height: 10%;
                    position: absolute;
                    left: 10%;
                    top: 10%;
                    border-radius: none;
                    z-index: 1;
                    overflow: hidden;
                    border: none;
                    outline: none;
                    padding: none;
                    margin: 0px;
                    border-radius: 3vh;
                    font-size: 2vh;
                }

                .bericht{
                    background-color: rgba(255, 255, 255, 1);
                    width: 80%;
                    height: 40%;
                    position: absolute;
                    left: 10%;
                    top: 25%;
                    border-radius: none;
                    z-index: 1;
                    overflow: hidden;
                    border: none;
                    outline: none;
                    padding: none;
                    margin: 0px;
                    border-radius: 3vh;
                    font-size: 2vh;
                    resize: none;
                }

                .naam:hover{
                    border: solid rgba(0, 92, 160, 1) 2px;
                }

                .bericht:hover{
                    border: solid rgba(0, 92, 160, 1) 2px;
                }

                .knop{
                    background-color: rgba(0, 99, 211, 1);
                    width: 80%;
                    height: 10%;
                    position: absolute;
                    left: 10%;
                    top: 70%;
                    border-radius: none;
                    z-index: 1;
                    overflow: hidden;
                    border: none;
                    border-radius: 3vh;
                    outline: none;
                    padding: none;
                    margin: 0px;
                    text-align: center;
                    font-size: 2vh;
                    border-bottom: solid rgba(0, 92, 160, 1) 0.5vh;
                }

                .knop:hover{
                    background-color: rgba(0, 92, 160, 1);
                }
            </style>
            <head>
                <title>Online Feedback</title>
            </head>
            <body>
                <div class="form">
                <textarea maxlength="140" placeholder="feedback voor """ + locatie_from_fun + """ " id="bericht" class="bericht"></textarea>
                <input type="text" maxlength="8" placeholder="naam" id="gebruiker" class="naam"></input>
                <button onclick="send()" class="knop">verstuur</button>
            </div>
                <script>
                    function send(){
                        newurl = document.URL;

                        feedback = document.getElementById('bericht').value;
                        naam = document.getElementById('gebruiker').value;

                        goodurl = newurl.split("?");

                        window.location.href = goodurl[0] + "?gebruiker=" + naam + "&bericht=" + feedback + "&locatie=" + " """ + locatie_from_fun + """ ";
                    }
                </script>
            </body>
        </html>
    """

    print(html)

    return html

if __name__ == '__main__':
    api.run(host="0.0.0.0", port=8000) 