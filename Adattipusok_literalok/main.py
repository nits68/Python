# A Python programozási nyelv fontosabb adattípusai
# =================================================
#  Az adattípus meghatározza a változóban tárolható értékek számát, típusát és értéktartományát
# Változó: Egy vagy több érték tárolására használt egység
# Változók jellemzői: adattípus, azonosító (név), kezdőérték, aktuális érték
# A literál olyan adat, melyhez nem rendelünk azonosítót, a megadás szintaxisa határozza meg a típusát

# 1. Egyszerű adattípusok: Egy érték tárolására alkalmasak
# 1.1 Szöveges adattípus és literál: str
from typing import List, Set, Tuple


szöveg: str = 'Python'
szöveg2: str = 'Jedlik'
print(type(szöveg))

# 1.2 Numerikus adattípusok: int, float és a literálok
egész: int = 68  # Egész érték tárolásához
valós: float = 3.14  # Valós érték tárolásához
print(type(egész))
print(type(valós))

# 1.3 Logikai adattípus: bool
logikai: bool = True  # Logikai értéket tárol, értéke csak True vagy False lehet

# 2. Összetett adattípusok: Több érték tárolását teszik lehetővé
# 2.1 Lista (egydimenziós tömb, vagy vektor más programozási nyelveken)
lista: List[str] = ['apple', 'banana', 'cherry']
print(lista)

# 2.2 Tuple (konstans listának tekinthető)
tuple: Tuple[str, str, str] = ('apple', 'banana', 'cherry')
print(tuple)

# 2.3 Halmaz (set, nem lehetnek azonos értékek)
halmaz: Set[str] = {'apple', 'banana', 'cherry'}
print(halmaz)

# 2.4 Számsorozat (range, for ciklusokhoz használjuk általában)
sor1: range = range(6)
print(sor1, end=' - ')
for i in sor1:
    print(i, end=' ')
print()

sor2: range = range(2, 8)
print(sor2, end=' - ')
for i in sor2:
    print(i, end=' ')
print()

sor3 = range(2, 15, 3)
print(sor3, end=' - ')
for i in sor3:
    print(i, end=' ')
print()
