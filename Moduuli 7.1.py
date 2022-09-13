
vuodenajat = ("talvi","talvi","talvi",
              "kevät","kevät","kevät",
              "kesä","kesä","kesä",
              "syksy","syksy","syksy")

syöttö = int(input("Anna kuukausi: "))
if syöttö > 11:
    muutos = syöttö-12
elif syöttö < 12:
    muutos = syöttö

vastaus = vuodenajat[muutos]


if vastaus in vuodenajat[0:3]:
    print("On talvi")

elif vastaus in vuodenajat[3:6]:
    print("On kevät")

elif vastaus in vuodenajat[6:9]:
    print("On kesä")

elif vastaus in vuodenajat[9:12]:
    print("On syksy")
