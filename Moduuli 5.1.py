import random
maara = int(input("Anna noppien määrä: "))
luvut = []
vastaus=0

for luku in range(maara):
    luvut.append(random.randint (1,6))

vastaus = vastaus + luvut[maara]
print ("Noppien lukujen yhteenlaskettu summa on: ", vastaus)
