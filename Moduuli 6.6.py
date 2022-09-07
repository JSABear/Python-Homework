#6
def pinta_ala(halkaisia):
    import math
    p_ala = math.pi * halkaisia * halkaisia
    return p_ala

def yksikkö_hinta(pinta_ala, hinta):
    y_hinta = pinta_ala / hinta
    return y_hinta

hinta1 = float(input("Anna pizzan 1 hinta: "))

halkaisia1 = float(input("Anna pizzan 1 halkaisia: "))

hinta2 = float(input("Anna pizzan 2 hinta: "))

halkaisia2 = float(input("Anna pizzan 2 halkaisia: "))

pizzap_ala1 = pinta_ala(halkaisia1)

pizzap_ala2 = pinta_ala(halkaisia2)

hintap_ala1 = yksikkö_hinta(pizzap_ala1,hinta1)

hintap_ala2 = yksikkö_hinta(pizzap_ala2,hinta2)

if hintap_ala1 > hintap_ala2:
    print ("Pizza 1 on parempi vastine rahalle.")

else:
    print ("Pizza 2 on parempi vastine rahalle.")