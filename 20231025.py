#import Szamrendszerek as szr
from Szamrendszerek import *

def SzamrendszerekKoztiValtas(szam, src_NumSys, dst_NumSys):
    if src_NumSys==10:
        str=tizesbolValtas(szam, dst_NumSys)
    elif dst_NumSys==10:
        str=tizesbeValt(szam, src_NumSys)
    else:
        str=tizesbeValt(szam, src_NumSys)
        str=tizesbolValtas(str, dst_NumSys)
    return str

x=SzamrendszerekKoztiValtas("101", 2, 2)
print(x)