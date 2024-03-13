"""
Hogyan néz ki amikor lefuttatjuk a programunkat?
- Ha megnézzük a teminált, akkor ezt látjuk alapból:
    - PS C:\[valami]\Documents\GitHub\2023_10b_python\20240306>
    - ez nyilván nálam néz ki, ez annak a mappának az elérése, amelyet megnyitottunk VSCode-dal
    - A > jel mellett "villog" a kurzor, hogy oda tudunk mindenféle paancsot beírni
        - Ezt hívjuk COMMAND PROMPT-nak, vagy röviden csak prompt
    - Mire jó a command prompt, mire tudjuk használni?
        - különböző parancsokat tudunk beírni, melyek lefutnak az enter megnyomása után
        - ezek a parancsok lényegében mini alkalmazások, használatuk, egyszerű
    - Milyen parancsokat írhatunk be? -néhány példa
        - cd mappanév   - belépés egy mappába
        - cd ..         - visszalépés előző mappába
        - ls vagy dir   - jelenlegi mappa tartalmának listázása
- Amikor lefuttatjuk az alkalmazásunkat, akkor a terminálban ezt a parancsot látjuk lefutni:
    - & C:/[valami]/python.exe c:/[valami]/Documents/GitHub/2023_10b_python/20240306/input1_feldolgozo.py
    - &: call operator, nem foglalkozunk vele
    - 2. helyen a python.exe elérési útja található
    - 3. helyen pedig a python file elérési útja van
- futtatás command prompt-ból
    - az előző parancsot is használhatjuk, de szerintem ez kényelmesebb módja a futtatásnak:
    - py input1_feldolgozo.py
        - py: hivatkozás a python programra egy rövid névvel
        - input1_feldolgozo.py a python fájlunk paraméterként átadva a python programnak
- saját programunk paramétere:
    - Az életünket nagyban megkönnyíthetjük, ha pl a beolvasandó fájl nevét paraméterként adjuk meg a programunknak
    - cél: ezt kelljen lefuttatni: "py input1_feldolgozo.py inputfile"
    - ekkor olvassa be a féjlt, s oldja meg vele a feladatokat
Futtassuk le ezt a programunkat!
    - py main.py inputfile
    - ezt irja ki: sys.argv: ['.\\main.py', 'inputfile']
    - A 0.index: a futtatott python file neve
    - Az 1. index: az első paraméterünk
Futtassuk újra 2 paraméter megadással:
    - py main.py inputfile input2
    - Ezt írja ki: sys.argv: ['.\\main.py', 'inputfile', 'input2']
    - tehát a sys.argv segítségével férünk hozzá a paraméterekhez!
"""

import sys

print(f"sys.argv: {sys.argv}")