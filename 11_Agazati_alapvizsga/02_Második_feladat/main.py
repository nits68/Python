# 1. Feladat: Töltsön fel egy listát kétjegyű egész számokkal!
# A lista elemszáma 10 legyen, a lista elemeit írja a képernyőre!
# Készítsen függvényt a prímszámok vizsgálatához!
# Egy számot akkor tekintünk prímszámnak, ha pontosan 2db
# különböző osztója van!
# A saját függvény felhasználásával döntse el, hogy van-e
# prímszám a listában!

# Megoldás:
# from typing import List
# import random


# def prime(szam: int) -> int:
#     osztok_szama: int = 0
#     for oszto in range(1, szam + 1):
#         if szam % oszto == 0:
#             osztok_szama += 1
#     return osztok_szama == 2


# ketjegyu_szamok: List[int] = []
# while len(ketjegyu_szamok) < 10:
#     ketjegyu_szamok.append(random.randint(10, 99))
# print(ketjegyu_szamok)

# van_prim = False
# for e in ketjegyu_szamok:
#     if prime(e):
#         van_prim = True
#         break
# if van_prim:
#     print('Van prímszám a listában!')
# else:
#     print('Nincs prímszám a listában!')

# 2. feladat: Egy string listát inicializáljon a hétköznapok kisbetűs neveivel!
#    ['hétfő', 'kedd', 'szerda', 'csütörtök', 'péntek']
# Készítsen függvényt, ami a paraméterében átadott nap nevének
# első karakterét nagybetűsre alakítja!
# A saját függvény felhasználásával írja ki a napok neveit
# a képernyőre fordított sorrendben!
# Minta: ['Péntek', 'Csütörtök', 'Szerda', 'Kedd', 'Hétfő']

# Megoldás:
# from typing import List


# def nagybetusre_alakit(nap: str) -> str:
#     # return str.capitalize(nap)
#     # vagy:
#     nagybetus: str = nap.upper()
#     return nagybetus[0] + nap[1:]


# napok: List[str] = ['hétfő', 'kedd', 'szerda', 'csütörtök', 'péntek']
# for i in range(len(napok)):
#     napok[i] = nagybetusre_alakit(napok[i])
# napok.reverse()
# print(napok)
