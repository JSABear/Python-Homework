def etsi(kentät):
    print("Voit palata alkuun kirjoittamalla: lopeta ")
    koodi = input("Anna lentokentän ICAO koodi: ")
    if koodi == "lopeta":
        return
    else:
        print(kentät[koodi])
        print("")
    return(kentät)


def syötä (kentät):
    print("Voit palata alkuun kirjoittamalla: lopeta ")
    lentokenttä = input("Anna lentokentän nimi: ")
    if lentokenttä == "lopeta":
        return
    else:
        koodikysely = input("Anna lentokentän ICAO koodi: ")
        if koodikysely == "lopeta":
            return
        else:
            kentät[koodikysely] = lentokenttä
            print()
    return(kentät)

lentokentät = {}

ohjelmaPäällä = 1
while ohjelmaPäällä ==1:

    print (f"Valikko\n1. Hae lentokenttää\n2. Lisää lentokenttä\n3. Lopeta  ")
    valinta = (int(input("Mitä tehdään?: ")))

    if valinta == 1:
        etsi (lentokentät)


    elif valinta == 2:
        syötä (lentokentät)

    elif valinta == 3:
        ohjelmaPäällä = 0
