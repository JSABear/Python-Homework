#1. vastaus
kuukaudet = {1:"Tammikuu", 2:"Helmikuu", 3:"Maaliskuu", 4:"Huhtikuu",
              5:"Toukokuu",6:"Kesäkuu",7:"Heinäkuu",8:"Elokuu", 9:"Syyskuu",
              10:"Lokakuu", 11:"Marraskuu", 12:"Joulukuu"}
vuodenajat = {1:"talvi", 2:"talvi", 3:"kevät", 4:"kevät",
              5:"kevät",6:"kesä",7:"kesä",8:"kesä", 9:"syksy",
              10:"syksy", 11:"syksy", 12:"talvi"}

kuukausi = int(input("Anna kuukauden numero:"))

if kuukausi in kuukaudet:
    print (kuukaudet[kuukausi]," on ", (vuodenajat[kuukausi])," kuukausi.")

