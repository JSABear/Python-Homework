#3
def muunnos(määrä):
    litra = määrä * 3.785
    return litra

while True:

    gallon = int(input("Anna gallon(US) määrä: "))
    if gallon < 0:
        break
    muutosLitra = muunnos(gallon)

    print (f"Litramäärä: {muutosLitra:.3f}")
