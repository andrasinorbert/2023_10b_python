file= open("input1")
sor= file.readline()
file.close()

#print(f"{sor};{type(sor)}")

sor=sor.strip() # sor elején/végén ha van sortörés vagy bármilyen whitespace karakter, eltünteti
sor_lista_str=sor.split(" ") # egy elválasztó karakter mentén felbontja a stringet, string tömbbel tér vissza
szamok=[]
for i in range(len(sor_lista_str)):
    szamok.append(int(sor_lista_str[i]))
print(szamok)