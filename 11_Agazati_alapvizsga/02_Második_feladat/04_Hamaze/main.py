import random
from typing import List


def halmaz_e(számok: List[int]) -> bool:
    segéd: List[int] = []
    for e in számok:
        if e not in segéd:
            segéd.append(e)
    return len(számok) == len(segéd)


def main() -> None:
    # Töltsön fel egy listát 5db egyjegyű véletlen számmal!
    # Írja a képernyőre a lista elemit!
    # Saját függvény készítésével döntse el, hogy a lista
    # tekinthető-e halmaznak (nincs benne ismétlődő érték)!
    # A feltöltést 10x ismételje meg és minden esetben
    # értékelje a feltöltött listákat a minta szerint!
    print('2. feladat: Halmaz-e?')
    for i in range(1, 11):
        számok: List[int] = []
        for _ in range(5):
            számok.append(random.randint(0, 9))
        print(f'{i:2}. {számok} -> Halmaznak {"" if halmaz_e(számok) else "nem "}tekinthető!')


if __name__ == "__main__":
    main()
