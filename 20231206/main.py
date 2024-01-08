f=open("2023_10b_python/20231206/input.txt", "r")
l=f.readlines()
f.close()

[print(x.strip()) for x in l]

print(l)