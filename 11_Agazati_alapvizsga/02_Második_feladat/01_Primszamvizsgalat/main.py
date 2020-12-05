# Feladat: Töltsön fel egy listát kétjegyű egész számokkal!
# A lista elemszáma 10 legyen, a lista elemeit írja a képernyőre!
# Készítsen függvényt prime azonosítóval a prímszámok vizsgálatához!
# (Egy számot akkor tekintünk prímszámnak, ha pontosan 2db különböző osztója van.)
# A prime() függvény felhasználásával döntse el, hogy van-e  prímszám a listában!

# Egy lehetséges megoldás:

from typing import List
import random


def prime(szam: int) -> int:
    osztok_szama: int = 0
    for oszto in range(1, szam + 1):
        if szam % oszto == 0:
            osztok_szama += 1
    return osztok_szama == 2


def main() -> None:
    ketjegyu_szamok: List[int] = []
    while len(ketjegyu_szamok) < 10:
        ketjegyu_szamok.append(random.randint(10, 99))
    print(ketjegyu_szamok)

    van_prim = False
    for e in ketjegyu_szamok:
        if prime(e):
            van_prim = True
            break
    if van_prim:
        print('Van prímszám a listában!')
    else:
        print('Nincs prímszám a listában!')


if __name__ == "__main__":
    main()
