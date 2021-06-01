from Épület import Épület


def main() -> None:
    # 3.1 Olvassa be az UTF-8 kódolású  legmagasabb.txt állományban lévő adatokat
    #  és tárolja el egy saját osztály típusú listában!
    # Ügyeljen rá, hogy az állomány első sora az adatok fejlécét tartalmazza!
    épületek: list[Épület] = []
    with open('legmagasabb.txt', 'r', encoding='utf-8') as file:
        for sor in file.read().splitlines()[1:]:
            épületek.append(Épület(sor))

    # 3.2 Határozza meg és írja ki a képernyőre a minta szerint,
    # hogy hány épület található az állományban!
    print(f'3.2 feladat: Épületek száma: {len(épületek)} db')

    # 3.3 Határozza meg és írja ki a képernyőre a minta szerint az állományba
    # található épületek emeleteinek az összegét!
    emeletek_összege: int = 0
    for e in épületek:
        emeletek_összege += e.emelet
    print(f'3.3 feladat: Emeletek összege: {emeletek_összege}')

    # 3.4 Határozza meg és írja ki a képernyőre a minta szerint, a legmagasabb épület
    #  adatait! Feltételezheti, hogy nem alakult ki holtverseny!
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

    # 3.5 Döntse el, hogy az adatok között található-e olasz épület!
    #  A keresését ne folytassa, ha a választ meg tudja adni!
    # A képernyőre írást a minta szerint végezze!
    van_olasz_épület: bool = False
    for e in épületek:
        if e.ország == 'Olaszország':
            van_olasz_épület = True
            break
    print(f'3.5 feladat: {"Van" if van_olasz_épület else "Nincs"} olasz épület az adatok között!')

    # 6. Készítsen statisztikát országok szerint az épületek számáról!
    # A képernyőre írást a minta szerint végezze!
    # print('6. feladat: Ország statisztika')
    # stat: Dict[str, int] = dict()
    # for e in épületek:
    #     if e.ország in stat:  # az ország, mint kulcs a szótárban található-e?
    #         # stat[e.ország] = stat[e.ország] + 1
    #         # vagy:
    #         stat[e.ország] += 1
    #     else:
    #         stat[e.ország] = 1
    # for key, value in stat.items():
    #     print(f'\t{key} - {value} db')

    # HF:
    # 7. feladat
    # Előző (szótáras) feladat megoldása szótár nélkül!
    # Utolsó feladat (nemet.txt)


if __name__ == "__main__":
    main()
