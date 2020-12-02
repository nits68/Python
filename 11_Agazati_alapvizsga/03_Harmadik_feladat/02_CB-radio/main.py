from CBadas import CBadas
from typing import List


print('CB-Rádió')
# 1. feladat: Olvassa be és tárolja el a cb.txt UTF-8 kódolású szöveges
#    állományban található adatokat!
#    Az összetartozó adatokat saját osztály definiálásával kezelje!
#    A fájl soraiban található adatokat saját osztály típusú listában tárolja!
#    Ügyeljen rá, hogy az állomány első sora a mezőneveket tartalmazza!

adasok: List[CBadas] = []
with open('cb.txt', 'r', encoding='UTF-8') as file:
    for sor in file.read().splitlines()[1:]:
        adasok.append(CBadas(sor))

# 2. feladat: Határozza meg és írja ki a képernyőre a minta szerint,
# hogy hány bejegyzés található a forrásállományban!
# Minta: 2. feladat: Bejegyzések száma: 381 db

print(f'2. feladat: Bejegyzések száma: {len(adasok)} db')

# 3. feladat: Határozza meg, hogy 'Sanyi' nevével hány bejegyzés van a forrásállományban!
sanyi_db: int = 0
for adas in adasok:
    if adas.nev == 'Sanyi':
        sanyi_db += 1
print(f'3. feladat: Sanyihoz tartozó bejegyzések: {sanyi_db} db')

# 4. feladat: Melyik sofőrhöz fűződik az egy percen belüli legtöbb adás?
# Jelenítse meg az adatsor adatait a képernyőn!
# Holtverseny esetén az összes adatsor jelenjen meg!
max_adas_darab: int = adasok[0].adas_db
for adas in adasok[1:]:
    if adas.adas_db > max_adas_darab:
        max_adas_darab = adas.adas_db
print('4. feladat: A legtöbb adás:')
for adas in adasok:
    if (adas.adas_db == max_adas_darab):
        print(f'\tIdő: {adas.ora}:{adas.perc} Darab: {adas.adas_db} Név: {adas.nev}')
