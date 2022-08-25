#1
#nimi = input("Mikä on sinun nimesi? ")
#print("Terve, " + nimi + "!")

#2
#import math
#säde = float(input("Anna ympyrän säde: "))
#pinta = math.pi * math.pow(säde, 2)
#print (f"Pinta-ala on: {pinta:6.2f}")

#3
#leveys   = float(input("Anna leveys: "))
#korkeus  = float(input("Anna korkeus: "))
#pinta    = (leveys * korkeus)
#piiri    = (leveys+leveys+korkeus+korkeus)
#print("Pinta ala on: " + str(pinta))
#print("Piiri on: " + str(piiri))

#4
#luku_1 = int(input("Anna ensimmäinen luku: "))
#luku_2 = int(input("Anna toinen luku: "))
#luku_3 = int(input("Anna kolmas luku: "))
#summa = luku_1 + luku_2 + luku_3
#kesk = summa / 3
#tulo = luku_1 * luku_2 * luku_3
#print("Summa on: " + str(summa))
#print("Keskiarvo on: " + str(kesk))
#print("Tulo on: " + str(tulo))

#5
#import math
#luotibase = float(input("Anna luoti määrä: "))
#naulabase = float(input("Anna naula määrä: "))
#leiviskäbase = float(input("Anna leiviskö määrä: "))
#luoti = (13.3)
#naula = (luoti * 32)
#leiviskä = (naula * 20)
#vastauskg = ((luotibase * luoti + naulabase * naula + leiviskäbase * leiviskä)/1000)
#gramma = (luotibase * luoti + naulabase * naula + leiviskäbase * leiviskä)
#grammaedit = str(vastauskg-int(vastauskg))[1:]
#grammashort = float(grammaedit)
#vastausg = grammashort * 1000
#print ("Massa nykymittojen mukaan: ")
#print (math.floor(vastauskg), ("kilogrammaa"),round(vastausg,2), ("grammaa"))

#6
#import random
#x_1 = random.randint (0,9)
#x_2 = random.randint (0,9)
#x_3 = random.randint (0,9)
#y_1 = random.randint (1,6)
#y_2 = random.randint (1,6)
#y_3 = random.randint (1,6)
#y_4 = random.randint (1,6)
#print("Kolminumeroinen koodisi on: " + str(x_1) + str(x_2)+ str(x_3))
#print("Nelinumeroinen koodisi on: " + str(y_1)  + str(y_2) + str(y_3) + str(y_4))