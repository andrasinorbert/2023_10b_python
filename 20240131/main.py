osszead=lambda num1, num2: num1+num2

def osszead2(num1, num2):
    return num1+num2
print(osszead(2,3))

hatvany=lambda num1, num2: num1**num2
print(hatvany(2,3))
negyzet=lambda num: hatvany(num, 2)
print(negyzet(5))

def osszegzes(lista:list, func):
    """Összegzés prog tétel.
    Paraméterek:
    lista: egy lista, mely int, float, string elemeket tartalmaz
    func: egy függvény, mely 2 paraméteres, ezt a műveletet végzi el a lista elemei közt
    return: olyan a tipusa, mint a listában az elemeké
    """
    s=lista[0]
    for i in range(1,len(lista)):
        s=func(s,lista[i])
    return s

# Listaelemek szorzata
print(osszegzes([1,2,3,4,5], lambda num1, num2: num1*num2))

def megszamlalas(lista:list, condition)->int:
    """
    condition: egy bool értékkel visszatérő 1 paraméteres függvény
    """
    c=0
    for i in range(len(lista)):
        if condition(lista[i]):
            c+=1
    return c

print(megszamlalas([1,2,3,4,5], lambda num:num<3))

def szelsoertek_kivalasztas(lista:list, condition)->tuple:
    """
    condition: 2 paraméteres függvény, mely összehasonlítja
        a jelenlegi max/min értéket a lista adott elemével
        visszatérési érteke: bool
    return: (index, érték)
    """
    ertek=lista[0]
    index=0
    for i in range(1, len(lista)):
        if condition(ertek,lista[i]):
            ertek=lista[i]
            index=i
    return index, ertek

# max kiválasztás
print(szelsoertek_kivalasztas([1,2,3,4,5], lambda jelenlegi,listaelem:jelenlegi<listaelem))

def kereses(lista:list, condition):
    """
    Keresés prog tétel
    condition: 1 paraméteres függvény, bool visszatéréssel
        keresett elem feltétele
    return: Ha találtunk megfelelő elemet, akkor (index, érték)
        Különben None
    """
    i=0
    while i<len(lista) and not condition(lista[i]):
        i+=1
    van=i<len(lista)
    if van:
        ertek=lista[i]
        index=i
        return index, ertek
    return None

print(kereses([1,2,3,4,5], lambda num:num==3))
print(kereses([1,2,3,4,5], lambda num:num==6))

def eldontes(lista:list, condition):
    """
    Eldöntés prog tétel
    condition: 1 paraméteres függvény, bool visszatéréssel
        keresett elem feltétele
    return: bool, ha találunk akkor True, egyébként False
    """
    i=0
    while i<len(lista) and not condition(lista[i]):
        i+=1
    van=i<len(lista)
    return van
print(eldontes([1,2,3,4,5], lambda num:num==3))
print(eldontes([1,2,3,4,5], lambda num:num==6))

def kivalasztas(lista:list, condition):
    """
    Kiválasztás prog tétel
    condition: 1 paraméteres függvény, bool visszatéréssel
        keresett elem feltétele
    return: A keresett elem (index, érték)
    """
    i=0
    while not condition(lista[i]):
        i+=1
    ertek=lista[i]
    index=i
    return index, ertek

print(kivalasztas([1,2,3,4,5],lambda num:num%2==0))