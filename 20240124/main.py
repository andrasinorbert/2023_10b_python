
def maximumkivalasztas(lista:list[int|float])->tuple[int,int|float]:
    """
        Maximum kiválasztás tétel.
        lista: int/float tartalmaz
        return[0]: index
        return[1]: max érték
    """
    max_index=0
    max_ertek=lista[0]

    for i in range(1,len(lista)):
        if max_ertek<lista[i]:
            max_ertek=lista[i]
            max_index=i
    return max_index, max_ertek

print(maximumkivalasztas([2,3,43,3]))
print(type(maximumkivalasztas([2,3,43,3])))


def osszegzes_osszeadassal(lista:list[int|float|str])->int|float|str:
    """
        Összegzés tétele.
        lista: int/float adatokat tárol

        return: az adatok összege
    """
    s=0
    for i in range(len(lista)):
        s+=lista[i]
    return s

# print(osszegzes(["egy","ketto", "három"])) nem működik: s int

def osszegzes_szorzassal(lista:list):
    s=1
    for i in range(len(lista)):
        s*=lista[i]
    return s

print(osszegzes_szorzassal([2,3,4]))

def osszegzes(lista:list, func):
    """
        Összegzés tétel általánosítva.
        func: az elemek közt végzendő művelet függvénye
    """
    s=lista[0]
    for i in range(1,len(lista)):
        s=func(s,lista[i])
    return s

def osszeadas(num1, num2):
    return num1+num2
def szorzas(num1, num2):
    return num1*num2
def osszefuz(str1, str2):
    return str1+str2
print(osszegzes([2,3,4],osszeadas))
print(osszegzes([2,3,4],szorzas))
print(osszegzes(["egy", "ketto"],osszefuz))


def szelsoertek_kivalasztas(lista:list, func)->tuple:
    """
        Max/Min kiválasztás tétel.
        lista: int/float tartalmaz
        func: listaelem és szélsőértéket összeasonlító függvény
        return[0]: index
        return[1]: szélsőérték
    """
    index=0
    ertek=lista[0]

    for i in range(1,len(lista)):
        if func(lista[i], ertek):
            ertek=lista[i]
            index=i
    return index, ertek

def kisebb(num1, num2):
    return num1<num2

print(szelsoertek_kivalasztas([2,3,4,3,2,0], kisebb))
print(szelsoertek_kivalasztas([2,3,4,3,2,0], lambda num1, num2 :num1<num2))

print(osszegzes([2,3,4], lambda num1, num2: num1+num2))

def megszamlalas(lista:list, t)->int:
    """
    t: 1 paraméteres függvény, bool-lal tér vissza

    """
    c=0
    for i in range(len(lista)):
        if t(lista[i]):
            c+=1
    return c

def oszthato_e_kettovel(num):
    return num%2==0
def oszthato_e(num, oszto):
    return num%oszto==0
def oszthato_e(num, oszto, maradek=0):
    return num%oszto==maradek
print(megszamlalas([1,2,3,4,5,6], oszthato_e_kettovel))
print(megszamlalas([1,2,3,4,5,6], lambda num:num%2==0))
print(megszamlalas([1,2,3,4,5,6], lambda num:num%3==1))