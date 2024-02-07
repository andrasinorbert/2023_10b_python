def beolvas(filename:str)->list[str]:
    """
    A fájl tartalmát soronként belepakolja egy listába
    """
    file=open(filename)
    sorok=file.readlines()
    file.close()
    return sorok

def strListToIntList(strList:list[str], start:int=0, end:int=0)->list[int]:
    """
    String listát Int listává alakít a strip() meghívásával
    start: az első számot tartalmazó sor
    end: az utolsó sorok száma, ami nem kerül feldolgozásra
    """
    szamok=[]
    for i in range(start,len(strList)-end):
        szam_str=strList[i].strip()
        szam=int(szam_str)
        szamok.append(szam)
    return szamok


sorok=beolvas("input3")
szamok=strListToIntList(sorok,1,1)
print(szamok)