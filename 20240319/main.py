import sys

print(sys.argv)

if len(sys.argv)<2:
    print("Nem adtál meg fájlnevet!")
    print("Helyes használat: py {sys.argv[0]} fájlnév")
else:
    filename= sys.argv[1]