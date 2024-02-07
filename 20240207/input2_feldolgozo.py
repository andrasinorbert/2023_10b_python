file=open("input2")
sorok=file.readlines()
file.close()

szamok=[]
for i in range(1,len(sorok)):
    szam_str=sorok[i].strip()
    szam=int(szam_str)
    szamok.append(szam)
print(szamok)

s=0
for i in range(len(szamok)):
    s+=szamok[i]
print(f"A számok összege: {s}")