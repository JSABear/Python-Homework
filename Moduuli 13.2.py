from flask import Flask, request
import mysql.connector

yhteys = mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        database='flight_game',
        user='root',
        password='8738',
        autocommit=True
        )

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
@app.route('/airport')

def airport():
    args = request.args
    icao = (args.get("airport"))
    sql_name = "Select name from airport where ident = '" + icao + "'"
    sql_munici = "Select municipality from airport where ident = '" + icao + "'"

    kursori = yhteys.cursor()
    kursori.execute(sql_name)
    sql_return_name = kursori.fetchone()

    kursori = yhteys.cursor()
    kursori.execute(sql_munici)
    sql_return_munici = kursori.fetchone()

    sql_print = {
        "ICAO": icao,
        "Name": sql_return_name[0],
        "Municipality": sql_return_munici[0]
    }

    return sql_print








if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)