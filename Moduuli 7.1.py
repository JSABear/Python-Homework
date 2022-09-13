
kuukaudet = ("joulkuu","tammikuu","helmikuu","maaliskuu","huhtikuu",
              "toukokuu","kesäkuu","heinäkuu","elokuu",
             "syyskuu","lokakuu","marraskuu")


syöttö = int(input("Anna kuukausi: "))
if syöttö > 11:
    muutos = syöttö-12
elif syöttö < 12:
    muutos = syöttö

vastaus = kuukaudet[muutos]


if vastaus in kuukaudet[0:3]:
    print("On talvi")

elif vastaus in kuukaudet[3:6]:
    print("On kevät")

elif vastaus in kuukaudet[6:9]:
    print("On kesä")

elif vastaus in kuukaudet[9:12]:
    print("On syksy")
