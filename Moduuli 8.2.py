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
maakoodi = input("Anna 2-kirjaiminen maakoodi: ")
sql = "SELECT TYPE, COUNT(*) FROM airport WHERE iso_country = '" + maakoodi + "' GROUP BY type"
print(sql)

#suoritetaan kysely
kursori = yhteys.cursor()
kursori.execute(sql)

#haetaan ja käsitellään tulosrivit
tulos = kursori.fetchall()
for rivi in tulos:
        print(f"{rivi[0]}, {rivi[1]}")

