# Fájlbeolvasás

def fajlbolOlvasas(_filename:str)->list:
    """
        Fájlból beolvassa az összes sort egy listába

        _filename: kiterjesztést is írj!
    """
    f=open(_filename, "r")
    lista=f.readlines()
    f.close()
    return lista

def listaTisztitas(_lista:list):
    """
        Modify _lista paraméter:
            strip()
    """
    for i in range(len(_lista)):
        _lista[i]=_lista[i].strip()

l=fajlbolOlvasas("input")
listaTisztitas(l)
print(l)