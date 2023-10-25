def tizesbeValt(szam,inputSzamrendszer):
    s=0
    for i in range(len(szam)):
        #print(f'karakter:{szam[(-1)*(i+1)]}')
        s+=int(szam[(-1)*(i+1)])* (inputSzamrendszer**i)
        #s+=int(szam[(-1)*(i+1)])* (pow(5,i))
    return str(s)

def tizesbolValtas(szam, dst_numSys, DEBUG=0):
    result=[]
    szam_src=int(szam)
    while szam_src >0:
        maradek=szam_src%dst_numSys
        if DEBUG: print(f'maradék: {maradek}')
        result.append(maradek)
        szam_src=int(szam_src/dst_numSys) # egészrész
        if DEBUG: print(f'szám: {szam_src}')

    if DEBUG: print(result)

    result_str=""
    #i=len(result)-1
    #while i>=0:
    for i in range(len(result)-1, -1, -1):
        #print(result[i])
        result_str+=str(result[i])
        #i-=1
    #print(result_str)
    print(f'A {szam} {dst_numSys} számrendszer beli alakja: {result_str}')
    return result_str