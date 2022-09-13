import mysql.connector

#yhteyden avaus
yhteys = mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        database='flight_game',
        user='root',
        password='8738',
        autocommit=True
        )

#määritetään kysely
icao = input("Anna ICAO koodi: ")
sql = "SELECT name, municipality FROM airport WHERE ident = '" + icao + "'"


#suoritetaan kysely
kursori = yhteys.cursor()
kursori.execute(sql)

#haetaan ja käsitellään tulosrivit
tulos = kursori.fetchall()
for rivi in tulos:
        print(f"{rivi[0]}, {rivi[1]}")