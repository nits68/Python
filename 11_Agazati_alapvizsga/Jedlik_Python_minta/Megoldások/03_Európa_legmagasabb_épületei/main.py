from typing import List
from Épület import Épület


def main() -> None:
    épületek: List[Épület] = []
    with open('legmagasabb.txt', 'r', encoding='UTF-8') as file:
        for sor in file.read().splitlines()[1:]:
            épületek.append(Épület(sor))

    print(f'3.2 feladat: Épületek száma: {len(épületek)} db')

    emeletek_összege: int = 0
    for e in épületek:
        emeletek_összege += e.emelet
    print(f'3.3 feladat: Emeletek összege: {emeletek_összege}')

    print('3.4 feladat: A legmagasabb épület adatai')
    legmagasabb_épület: Épület = épületek[0]
    for e in épületek[1:]:
        if e.magasság > legmagasabb_épület.magasság:
            legmagasabb_épület = e
    print(f'\tNév: {legmagasabb_épület.név}')
    print(f'\tVáros: {legmagasabb_épület.város}')
    print(f'\tOrszág: {legmagasabb_épület.ország}')
    print(f'\tMagasság: {legmagasabb_épület.magasság} m')
    print(f'\tEmeletek száma: {legmagasabb_épület.emelet}')
    print(f'\tÉpítés éve: {legmagasabb_épület.épült}')

    van_olasz_épület: bool = False
    for e in épületek:
        if e.ország == 'Olaszország':
            van_olasz_épület = True
            break
    print(f'3.5 feladat: {"Van" if van_olasz_épület else "Nincs"} olasz épület az adatok között!')


if __name__ == "__main__":
    main()
