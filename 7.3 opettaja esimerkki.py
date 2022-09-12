def choose():
    print("1 Anna uusi")
    print("2 hae")
    print("0 lopeta")
    choice = -1
    while choice < 0 or choice > 2:
        choice = int(input("Valitse: "))
    return choice


def add_new(airports):
    icao = input("Aseman ICAO koodi: ")
    name = input("Aseman nimi: ")
    airports[icao] = name


def search(airports):
    icao = input("Aseman ICAO koodi: ")
    if icao in airports:
        print(airports[icao])
    else:
        print("Tuntemanton koodi")


airport_list= {}
choice = choose()
while choice != 0:
    if choice == 1:
        add_new(airport_list)
    elif choice == 2:
        search(airport_list)
    choice = choose()
