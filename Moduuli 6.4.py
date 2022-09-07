#4
def laske(luvut):
    vastaus = 0
    for num in range(0,len(luvut)):
        vastaus = vastaus + luvut[num]
    return vastaus
lista=[1,2,3,4]
yhteenlasku = laske(lista)
print ("vastaus on: ",yhteenlasku)

