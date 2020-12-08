from Versenyző import Versenyző
from typing import Any, List, cast


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
    nőiBajnok: Any = None
    for v in fg2016:
        if v.ketegória == 'Noi':
            if nőiBajnok is None:
                nőiBajnok = v
            if isinstance(nőiBajnok, Versenyző):
                if v.összpont() > cast(Versenyző, nőiBajnok).összpont():
                    nőiBajnok = v

    print(f'6. feladat: A bajnok női versenyző: {cast(Versenyző, nőiBajnok).név}')


if __name__ == "__main__":
    main()
