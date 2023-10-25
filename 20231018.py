

src=5
szam="423"

def tizesbeValt(szam,inputSzamrendszer):
    s=0
    for i in range(len(szam)):
        #print(f'karakter:{szam[(-1)*(i+1)]}')
        s+=int(szam[(-1)*(i+1)])* (inputSzamrendszer**i)
        #s+=int(szam[(-1)*(i+1)])* (pow(5,i))
    return s

x=tizesbeValt("765", 8)
print(x)