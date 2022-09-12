#2
nimet = set()
ohjelmaPäällä = 1
while ohjelmaPäällä==1 :
    syöttö = (input("Anna nimi: "))
    if syöttö in nimet:
        print("Annoit saman nimen.")
    elif syöttö == "":
        print(nimet)
        ohjelmaPäällä = 0
    else:
        nimet.add(syöttö)
        print("uusi nimi")
else:
    ohjelmaPäällä = 0

