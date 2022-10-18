import psycopg2

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