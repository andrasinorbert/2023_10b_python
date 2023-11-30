"""
lista_db=int(input("Add meg hány elemű legyen a lista: "))
print("Töltsd fel a listát!")

lista=[]
for i in range(lista_db):
    x=int(input(f"Add meg a(z) {i+1}.elemet: "))
    lista.append(x)
else:
    print(lista)
"""

def lista_kiir(l, sorElejiString=""):
    s=sorElejiString
    for i in range(len(l)):
        s+=str(l[i])+" "
    print(s)

def matrix_kiir(l, mindenSorElejiString=""):
    for i in range(len(l)):
        lista_kiir(l[i],str(i+1)+mindenSorElejiString)

def lista_osszeg(l):
    s=0
    for i in range(len(l)):
        s+=l[i]
    return s

lista_db=int(input("Add meg hány listát szeretnél megadni: "))
lista_elem_db=int(input("Add meg hány elemű legyen a lista: "))
print("Töltsd fel a listát!")

lista=[]

print("Add meg az elemek értékeit!")
for i in range(lista_db):
    print(f"{i+1}.lista:")
    l=[]
    for j in range(lista_elem_db):
        print(f"\t{j+1}.elem:", end=" ")
        x=int(input())
        l.append(x)
    lista.append(l)

matrix_kiir(lista, ".sor: ")

for i in range(len(lista)):
    print(f"{i+1}. lista összege:",
          lista_osszeg(lista[i]),
          sep=" ")