file=open("input1")
sorok=file.readlines()
file.close()

print(sorok)

szamok=[]
for i in range(len(sorok)):
    print(f"({sorok[i]})\t{type(sorok[i])}")
    szam_str=sorok[i].strip()
    print(f"{szam_str}\t{type(szam_str)}")
    szam=int(szam_str)
    print(f"{szam}\t{type(szam)}")
    szamok.append(szam)

print(szamok)

szamok=[]
for i in range(len(sorok)):
    szamok.append(int(sorok[i].strip()))
print(szamok)