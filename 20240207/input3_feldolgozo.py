file=open("input3")
sorok=file.readlines()
file.close()

szamok=[]
for i in range(1,len(sorok)-1):
    szam_str=sorok[i].strip()
    szam=int(szam_str)
    szamok.append(szam)
print(szamok)