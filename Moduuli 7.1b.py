#1. vaihtoehtoinen tapa ilman sanakirjaa
def määritä(kuukausi):
    if kuukausi == 12 or kuukausi == 1 or kuukausi == 2:
        määritettyaika = 1
    elif kuukausi > 2 and kuukausi < 6:
        määritettyaika = 2
    elif kuukausi > 5 and kuukausi < 9:
        määritettyaika = 3
    else:
        määritettyaika = 4
    return(määritettyaika)

vuodenaika=0

kuukausi = int(input("Anna kuukauden numero:"))

määritettyaika = määritä(kuukausi)
vuodenaika = määritettyaika

if vuodenaika ==1:
    print("On talvi.")
elif vuodenaika ==2:
    print("On kevät.")
elif vuodenaika == 3:
    print("On kesä.")
else:
    print("On syksy.")