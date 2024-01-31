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

def megszamlalas(lista:list)->int:
    pass
