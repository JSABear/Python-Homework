


luku = int(input("Anna kokonaisluku: "))
if luku>1:
    for i in range(2,luku//2):
        if(luku%i)==0:
            print(luku,"Ei ole alkuluku.")
            break
    else:
        print(luku,"On alkuluku.")
else:
    print(luku,"Väärä syöttö.")