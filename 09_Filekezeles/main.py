from typing import List


print('Szövges állományok írása és olvasása')

# UTF-8 kódolású szöveges állományok olvasása:
# try-except szerkezet elhagyható, ha a vizsgafeladatban nem kérik, de a gyakorlatban erősen javasolt a használata
# (Az állomány sorait egy str típusú listába olvassuk be az open() függvénnyel és a with-as utasítással:
# Beolvasás közvetlenül szöveges típusú listába a read() és splitlines() metódusokkal
sorok: List[str] = list()
try:
    with open('forras.txt', 'r', encoding='UTF-8') as file:
        sorok = file.read().splitlines()
except Exception as ex:
    print(f'Hiba: {ex}')
print(sorok)

# Beolvasás szám típusú listába a readlines() metódussal + konverzió:
szamok: List[int] = list()
try:
    with open('szamok.txt', 'r', encoding='UTF-8') as file:
        for e in file.readlines():
            szamok.append(int(e.strip()))  # a strip() mtódus a '\n' vezérlő karaktert törli, int() konvertál
        # vagy rövidítve:
        # szamok = [int(e.strip()) for e in file.readlines()]
except Exception as ex:
    print(f'Hiba: {ex.__doc__}')
print(szamok)

# Beolvasás soronként a readline() metódussal:
szamok2: List[int] = list()
try:
    with open('szamok.txt', 'r', encoding='UTF-8') as file:
        sor: str = 'x'
        while sor:
            sor: str = file.readline()
            if sor != '':
                szamok2.append(int(sor))
except Exception as ex:
    print(f'Hiba: {ex.__doc__}')
print(szamok2)

# Az open() függvény második paramétere a megnyitás módját határozza meg:
# - 'r' - Read - Alapértelmezett érték. Olvasásra nyitja meg az állományt, hibát dob, ha a file nem létezik.
# - 'a' - Append - Állomány megnyitása hozzáfűzésre, ha az állomány nem létezik, akkor létrehozza
# - 'w' - Write - Írásra nyitja meg az állományt, létező állományt felülír, ha az állomány nem létezik, akkor létrehozza
# - 'x' - Create - Létrehozza az állományt íráshoz, hibát dob, ha a file létezik.

# Szöveges állokmányok írása
# - írás soronként a write() metódussal:

try:
    with open('cél.txt', 'w', encoding='UTF-8') as file:
        for e in sorok:
            file.write(f'{e}\n')  # A sorvég '\n' vezérlő karakter hozzáfűzése általában szükséges
except Exception as ex:
    print(f'Hiba: {ex}')

# - teljes lista (sorok) kiírása a writelines() metódussal (a '\n' vezérlő karaktereket minden sor végéhez kell fűzni):

try:
    with open('cél2.txt', 'w', encoding='UTF-8') as file:
        ki: List[str] = []
        for e in sorok:
            ki.append(f'{e}\n')
        file.writelines(ki)
        # vagy röviden:
        # file.writelines([f'{e}\n' for e in sorok])
except Exception as ex:
    print(f'Hiba: {ex}')
