#2
def heita(x):
    import random
    luku = random.randint(1,x)
    print(luku)
    return luku
saatu=0
sivut= int(input("Anna nopan sivujen lukumäärä:" ))
while True:
    saatu=heita(sivut)
    if saatu ==sivut:
        break