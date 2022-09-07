#5
def parsi(luvut):
    parsittuLista = list(filter(lambda x: x % 2 == 0, luvut))


    return parsittuLista

lista = [1,2,3,4,5,6,7,8,9,10]

parsittuLista = parsi(lista)

print("Parsimaton lista: ",lista)
print("Parsittu lista: ",parsittuLista)