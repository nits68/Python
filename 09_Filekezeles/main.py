from typing import List


print('Szövges állományok kezelése')

# UTF-8 kódolású szöveges állományok olvasása:
# (Az állomány sorait egy str típusú listába olvassuk be az open() függvénnyel és a with-as utasítással:
sorok: List[str] = list()
with open('forras.txt', 'r', encoding='UTF-8') as file:
    try:
        sorok = file.read().splitlines()
    except Exception as ex:
        print(f'Hiba: {ex.__doc__}')
print(sorok)

# Az open() függvény második paramétere a megnyitás módját határozza meg:
# - 'r' - Read - Alapértelmezett érték. Olvasásra nyitja meg az állományt, hibát dob, ha a file nem létezik.
# - 'a' - Append - Állomány megnyitása hozzáfűzésre, ha az állomány nem létezik, akkor létrehozza
# - 'w' - Write - Írásra nyitja meg az állományt, létező állományt felülír, ha az állomány nem létezik, akkor létrehozza
# - 'x' - Create - Létrehozza az állományt íráshoz, hibát dob, ha a file létezik.

# Szöveges állokmányok írása
# - írás soronként a write() metódussal:
with open('cél.txt', 'w', encoding='UTF-8') as file:
    try:
        for e in sorok:
            file.write(f'{e}\n')
    except Exception as ex:
        print(f'Hiba: {ex.__doc__}')

# - teljes lista kiírása a writelines() metódussal (a '\n' vezérlő karaktereket minden sor végéhez kell fűzni):
with open('cél2.txt', 'w', encoding='UTF-8') as file:
    try:
        file.writelines([f'{e}\n' for e in sorok])
    except Exception as ex:
        print(f'Hiba: {ex.__doc__}')
