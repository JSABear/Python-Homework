#1
#luku = 3
#while luku < 1000:
#    print (luku)
#    luku += 3

#2
#vastaus = float(input("Määrä tuumia: "))
#while vastaus > 0:
#    print (vastaus * 2.51, "senttiä")
#    break
#else:
#    print ("")

#3
#lukujono = []
#luku = 0
#while luku != "":
#    luku = input("Anna luku: ")
#    lukujono.append(luku)
#else:
#    lukujono.remove("")
#    print("Pienin luku on:", min(lukujono))
#    print("Suurin luku on:", max(lukujono))

#4
#import random
#oikein = random.randint(1, 10)
#arvaus = int(input("Anna arvaus 1-10 välillä: "))
#while oikein != "arvaa":
#    print
#    if arvaus < oikein:
#        print ("Liian pieni vastaus")
#        arvaus = int(input("Anna arvaus 1-10 välillä: "))
#    elif arvaus > oikein:
#        print ("Liian suuri vastaus")
#        arvaus = int(input("Anna arvaus 1-10 välillä: "))
#    else:
#        print ("Oikein")
#        break

#5
#usr = "käyttäjä"
#psswrd = "salasana"
#yritys = 0
#while True:
#    usr = input("Anna käyttäjätunnus: ")
#    psswrd = input("Anna salasana: ")
#    if usr == "käyttäjä" and psswrd == "salasana":
#        print("Tervetuloa")
#        break
#    elif usr != "1" or psswrd != "2":
#        print(f"Väärin, {4 - yritys} yritystä jäljellä")
#        yritys += 1
#    if yritys == 5:
#        print("Pääsy evätty")
#        break

#6 Ei tehty
