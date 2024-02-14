import fuggvenyek as f

sorok= f.beolvas("input3")
print(sorok)
szamok_str=sorok[0].split(" ")
print(szamok_str)
szamok= f.strListToIntList(szamok_str,1)
print(szamok)