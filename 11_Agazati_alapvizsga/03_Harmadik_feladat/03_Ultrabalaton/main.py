from Eredmény import Eredmény
from typing import List


def main() -> None:
    # 1. Olvassa be az ub2017egyeni.txt állományban lévő adatokat és tárolja el
    # egy saját osztály típusú listában!
    # Ügyeljen arram, hogy az állomány első sora a mezőneveket tartalmazza.

    ub2017: List[Eredmény] = []
    with open('ub2017egyeni.txt', 'r', encoding='utf-8') as file:
        for sor in file.read().splitlines()[1:]:
            ub2017.append(Eredmény(sor))

    # 2. Határozza meg és írja ki a minta szerint a képernyőre
    # a versenyen elindult futók számát!
    # Minta: 2. feladat: Futók száma: 186

    print(f'2. feladat: Futók száma: {len(ub2017)}')

    # 3. Számolja meg és írja ki a képernyőre a minta szerint,
    # hogy hány női sportoló teljesítette a teljes távot!
    nők100: int = 0
    for e in ub2017:
        if e.ketegória == 'Noi' and e.táv_százalék == 100:
            nők100 += 1
    print(f'3. feladat: Célba érkező női sportolók: {nők100} fő')

    # 4. feladat: Határozzuk meg a leghosszabb nevű futót/futókat és és írjuk ki az adatait a minta szerint!
    # Holtverseny esetén csak a futok neveit írjuk egymás mellé a minta szerint!
    print('4. feladat: A leghosszabb nevű futó(k)')
    # 4.1 Meghatározzuk a leghosszabb név hosszát:
    név_hossz_max: int = 0
    for e in ub2017:
        # if e.név_hossz() > név_hossz_max:
        #     név_hossz_max = e.név_hossz()
        # vagy:
        if len(e.név) > név_hossz_max:
            név_hossz_max = len(e.név)

    # 4.2 Kiválogajuk egy új listába a leghosszabb nevű futókat:
    ub2017_max: List[Eredmény] = []
    for e in ub2017:
        if e.név_hossz() == név_hossz_max:
            ub2017_max.append(e)

    # Az új lista (ub2017_max) hossza szerint elvégezzük az eredmény kiírását
    if len(ub2017_max) == 1:
        print(f'\tNév: {ub2017_max[0].név}')
        print(f'\tRajtszám: {ub2017_max[0].rajtszám}')
        print(f'\tEredmény: {ub2017_max[0].idő}')
    else:
        print('\tNevek: ', end='')
        for e in ub2017_max:
            print(f'{e.név}', end='; ')
        print()  # soremelés az utolsó futó neve után

    # 5. Határozza meg és írja ki a minta szerint a teljes távot teljesítő
    # férfi sportolók átlagos idejét órában!
    # Feltételezheti, hogy legalább egy ilyen sportoló volt.
    férfi100_összeg_idő: float = 0
    férfi100_fő: int = 0
    for e in ub2017:
        if e.ketegória == 'Ferfi' and e.táv_százalék == 100:
            férfi100_fő += 1
            férfi100_összeg_idő += e.idő_óra()
    print(f'5. Férfi sportolók átlagos ideje: {férfi100_összeg_idő / férfi100_fő} óra')


if __name__ == "__main__":
    main()
