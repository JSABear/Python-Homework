#2
luku = 0
lukujono = []

while luku != "":
    luku = input("Anna luku: ")
    lukujono.append(luku)
else:
    lukujono.remove("")

lukujono.sort(reverse=True)
print(lukujono[0:5])
