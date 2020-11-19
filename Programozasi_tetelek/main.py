import random
from typing import List

# 1 Összetett adatszerkezet feltöltésének módjai

# 1.1 Feltöltés felhasználói input útján:
# nevek: List[str] = list()
# print('Kérem a neveket 0-végjelig!')
# inputNév: str = ''
# while inputNév != '0':
#     inputNév = input('Név: ')
#     if inputNév != '0' and len(inputNév) != 0:
#         nevek.append(inputNév)
# print(nevek)

# 1.2 Feltöltés véletlen értékekkel:
szamok: List[int] = []
for i in range(5):
    szamok.append(random.randint(10, 99))

# 1.3 Feltöltés literálokkal:
allitasok: List[bool] = [True, True, False, True, False]
print(allitasok)

# 1.4 Feltöltés szöveges állományból:
# Később fogjuk tanulni!

# 2 Összetett adatszerkezet bejárása
# Vizsgálathoz, műveletekhez rendre "elővesszük" az összetett adatszerkezet elemeit
# 2.1 Nincs szükség az elem indexére
for i in szamok:
    print(i, end=' ')
print()

# 2.2 Értékek (szamok[i]) és indexek (i) rendelkezésre állnak
for i in range(len(szamok)):
    print(f'szamok[{i}] = {szamok[i]} ')

# Vagy: Értékek (item) és indexek (index) rendelkezésre állnak
for index, item in enumerate(szamok):
    print(f'szamok[{index}] = {item}', end=' ')
print()

# 3 Egy sorozathoz egy értéket rendelő programozási tételek
# 3.1 Eldöntés tétele: Megadott tulajdonságú érték megtalálható-e a listában?
# Feladat: Döntse el, hogy található-e páratlan szám a listában!
# A keresést ne folytassa, ha a választ megtudja adni!

vanParatlan: bool = False  # Feltételezzük, hogy nincsen páratlan szám a listában
for szam in szamok:
    if szam % 2 == 1:
        vanParatlan = True
        break
# Kiírás lehetőségei
if vanParatlan:
    print('A listában van páratlan szám!')
else:
    print('A listában nincs páratlan szám!')
# vagy:
print('A listában ' + ('van' if vanParatlan else 'nincs') + ' páratlan szám!')
# vagy:
print(f'A listában {"van" if vanParatlan else "nincs"} páratlan szám!')

# 3.2 Megszámlálás tétele: Megadott tulajdonságú értékek darabszáma
# Feladat: Határozzuk meg az ötvennél nagyobb páros számok darabszámát!
db_paros_50: int = 0
for i in szamok:
    if i % 2 == 0 and i > 50:
        db_paros_50 += 1
print(f'Ötvennél nagyobb páros számok darabszáma: {db_paros_50}')

# 3.3 Összegzés tétele: Megadott tulajdonságú értékek összege/átlaga
# Feladat: Határozzuk meg az 5-el osztható számok átlagát!
db_oszt5: int = 0
osszeg_oszt5 = 0
for i in szamok:
    if i % 5 == 0:
        db_oszt5 += 1
        osszeg_oszt5 += i
if db_oszt5 == 0:
    print('Nincs a listában 5-el osztható szám!')
else:
    print(f'Az 5-el osztható számok darabszáma: {db_oszt5}')
    print(f'Az összegük: {osszeg_oszt5} és az átlaguk: {osszeg_oszt5 / db_oszt5}')

# 3.4 Szélsőérték (minimum, maximum) keresése
# 3.4.1 Csak a legnagyobb elem értékét kell meghatározni:
# Feladat: Határozzuk meg a legnagyobb elem/elemek értékét!
max: int = szamok[0]  # Kinevezzük az első elemet a legnagyobbnak
for szam in szamok[1:]:  # szamok[1:] -> Az első elemet elhagyjuk, önmagához nem hasonlítjuk
    if szam > max:
        max = szam
print(f'A legnagyobb szám értéke: {max}')

# 3.4.2 A legnagyobb elem értéke és az indexe is kell:
# Feladat: Határozzuk meg a legkisebb elem értékét és indexét!
# Holtverseny esetén elegendő az elsőt megadnia.

mini: int = 0  # Kinevezzük az első elemet a legkisebbnek
for i in range(1, len(szamok)):
    if szamok[i] < szamok[mini]:
        mini = i
print(f'A legkisebb szám értéke: {szamok[mini]}, indexe: {mini}')

# 3.4.3 A holtversenyt is kezelni kell
# Feladat: Holtverseny esetén írjuk ki az összes elem indexét
print('Legkisebb elem(ek) indexei:', end=' ')
for i, item in enumerate(szamok):
    if (item == szamok[mini]):
        print(i, end=' ')
print()

# 3.4.4 Nem nevezhető ki az első elem a legkisebb/legnagyobb elemnek
# Feladat: Határozzuk meg a legnagyobb páratlan szám értékét és indexét a listában!
maxi_paratlan: int = -1  # Ha -1 marad az értéke, akkor nincs páratlan szám a listában
for i, item in enumerate(szamok):
    if item % 2 == 1:  # Ha páratlan
        if maxi_paratlan == -1:  # Első páratlan szám a listában
            maxi_paratlan = i  # Kinevezzük a legnagyobb páratlan számnak
        else:
            if item > szamok[maxi_paratlan]:
                maxi_paratlan = i
if maxi_paratlan == -1:
    print('Nincs a listában páratlan szám!')
else:
    print(f'A legnagyobb páratlan szám értéke: {szamok[maxi_paratlan]}, indexe: {maxi_paratlan}')

# 4 Egy sorozathoz egy sorozatot rendelő programozási tételek
# 4.1 Kiválogatás
# Feladat: Válogassuk ki a 3-al osztható számokat!
oszhato3al: List[int] = []
for i in szamok:
    if i % 3 == 0:
        oszhato3al.append(i)
print(f'A 3-al osztható számok: {oszhato3al}')

# 4.2 Rendezés
# Feladat: Rendezzük a lista elemeit a buborékos rendezés algoritmusával!
for ig in range(len(szamok) - 1, 0, -1):  # ig -> 9..1
    csere_volt: bool = False
    for i in range(ig):  # i -> 0..8 / 0..7 / 0..6 / ... / 0..0/
        if (szamok[i] > szamok[i+1]):  # Cserélni kell az egymás mellett álló elemeket
            csere: int = szamok[i]  # segédváltozó két érték felcseréléséhez
            szamok[i] = szamok[i+1]
            szamok[i+1] = csere
            csere_volt = True
    if csere_volt is False:  # Ha nem volt csere, akkor rendezett a lista, kiléphetünk
        break
print(f'Rendezve: {szamok}')


# 5 Egy sorozathoz két sorozatot rendelő programozási tételek
# 5.1 Szétválogatás
# Válogassuk szét a páros és páratlan számokat!
paros_szamok: List[int] = []
paratlan_szamok: List[int] = []
for i in szamok:
    if i % 2 == 0:
        paros_szamok.append(i)
    else:
        paratlan_szamok.append(i)
print(f'A páros lista: {paros_szamok}')
print(f'A páratlan lista: {paratlan_szamok}')

# 6 Két sorozathoz egy sorozatot rendelő programozási tételek
# 6.1 Összefuttatás (rendezettek uniója)
# 6.2 Egyesítés (unió)
# 6.3 Metszet
