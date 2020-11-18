# Iteráció (ciklus)
# Olyan vezérlési szerkezet, melyet utasítások ismétlésére használunk
# Ciklusok fajtái:
# - klasszikus növekményes ciklus (for, NINCS a Python-ban)
# - for-in ciklus (speciális ciklus a Python-ban, foreach ciklushoz hasonlít leginkább)
# - elöltesztelő ciklus (while)
# - hátultesztelő ciklus (NINCS a Python-ban)
import random  # random modul, véletlen számok generálásához

# Klasszikus növekményes ciklus megvalósítása for-in ciklussal:
for i in range(8):  # range osztály számsorozatot állít elő (0, 1, 2, 3, ..., 6, 7)
    print(i, end=' ')  # 0 1 2 3 4 5 6 7
print()

for i in range(-5, 5):
    print(i, end=' ')  # -5 -4 -3 -2 -1 0 1 2 3 4
print()

for i in range(1, 11, 2):
    print(i, end=' ')  # 1 3 5 7 9
print()

t = ['alma', 'körte', 'szilva']  # lista, összetett adatszerkezet, több adatot tárol
for i in range(len(t)):
    print(f't[{i}]={t[i]}', end=' ')
print()

# Elöltesztelő ciklus példa: lottószámok generálása
lotto90 = set()  # Halmaz
while len(lotto90) < 5:
    lotto90.add(random.randint(1, 90))  # 1 >= vélszám <= 90
print(lotto90)

# Halmaz elemei növekvő sorrendben tartalmazás vizsgálattal:
lotto90rendezve = []
for i in range(1, 91):  # 1..90
    if i in lotto90:
        lotto90rendezve.append(i)
print(lotto90rendezve)

# A break utasítás: segítségével kiléphetünk a ciklusból,
# befejezzük az ismétlést a ciklusfeltétel tesztelése nélkül.
print('A break utasítás')
i = 1
while i < 6:
    print(i, end=' ')
    if i == 3:
        break
    i += 1
print()

# A continue utasítás: segítségével befejezzük a ciklusmag aktuális végrehajtását,
# a ciklusfeltétel (i < 6) tesztelésével folytatjuk a kódot
print('A continue utasítás')
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i, end=' ')
print()
