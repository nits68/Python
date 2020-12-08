from Versenyző import Versenyző
from typing import List, cast


def main() -> None:
    # 1. Olvassa be a fob2016.txt állományban lévő adatokat és tárolja el egy
    # saját osztály típusú listában!
    fg2016: List[Versenyző] = []
    with open('fob2016.txt', 'r', encoding='UTF-8') as file:
        for sor in file.read().splitlines():
            fg2016.append(Versenyző(sor))

    # 2. Határozza meg és írja ki a képernyőre a minta szerint, hogy
    # hány versenyző indult összesen a két kategóriában a bajnokságon!
    print(f'2. feladat: Versenyzők száma: {len(fg2016)} fő')

    # 3. Határozza meg és írja ki a képernyőre a minta szerint
    #  a női versenyzők arányát az összes versenyzőszámhoz képest!
    # A százalékos értéket két tizedesjegy pontossággal jelenítse meg!
    # Feltételezheti, hogy legalább egy női versenző indult a bajnokságban.
    női_versenyzők_száma: int = 0
    for v in fg2016:
        if v.ketegória == 'Noi':
            női_versenyzők_száma += 1
    arány_nők: float = női_versenyzők_száma / len(fg2016) * 100
    print(f'3. feladat: A női versenyzők aránya: {arány_nők:.2f} %')

    print(fg2016[1].összpont())

    # 5. Határozza meg és írja ki a minta szerint a 2016-os footgolf bajnokság legtöbb pontot
    # szerzett női bajnokát! Feltételezheti, hogy legalább egy női induló volt a bajnokságon, és
    # nem alakult ki holtverseny.
    női_bajnok = None
    for v in fg2016:
        if v.ketegória == 'Noi':
            if női_bajnok is None:
                női_bajnok = v
            else:
                if v.összpont() > női_bajnok.összpont():
                    női_bajnok = v

    print(f'5. feladat: A bajnok női versenyző: {cast(Versenyző, női_bajnok).név}')

    női_maxi = -1
    for i, v in enumerate(fg2016):
        if v.ketegória == 'Noi':
            if női_maxi == -1:
                női_maxi = i
            else:
                if v.összpont() > fg2016[női_maxi].összpont():
                    női_maxi = i

    print(f'5. feladat: A bajnok női versenyző: {fg2016[női_maxi].név}')

    női_versenyzők: List[Versenyző] = []
    for v in fg2016:
        if v.ketegória == "Noi":
            női_versenyzők.append(v)

    női_bajnok2: Versenyző = női_versenyzők[0]
    for v in női_versenyzők[1:]:
        if v.összpont() > női_bajnok2.összpont():
            női_bajnok2 = v
    print(f'5. feladat: A bajnok női versenyző: {női_bajnok2.név}')


if __name__ == "__main__":
    main()
