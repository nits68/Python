def main() -> None:
    # Alapfogalmak: program, algoritmus, változó, adatszerkezet, literál
    # ==================================================================
    # program = algoritmus + adatszerkezet
    # algoritmus = utasítások végrehajtásának sorrendje, amit vezérlési szerkezetek határoznak meg a programozási nyelvekben
    # változók = adatok tárolására használt egységek
    # változók jellemzői:
    # - azonosító (változó neve)
    # - adattípus (str, int, float, bool, stb., Python-ban megadásuk opcionális)
    # - kezdőérték
    # - aktuális érték
    # adatszerkezet = programban használt változók halmaza
    # literál = olyan adat, melyhez nem rendelünk azonosítót, a megadás szintaxisa határozza meg a típusát

    # A Python programozási nyelv fontosabb adattípusai
    # =================================================
    #  Az adattípus meghatározza a változóban tárolható értékek számát, típusát és értéktartományát

    # 1. Egyszerű adattípusok: Egy érték tárolására alkalmasak
    # 1.1 Szöveges adattípus és literál: str

    szoveg: str = 'Python'
    szoveg2: str = "Jedlik"
    print(szoveg + ' ' + szoveg2)
    print(type(szoveg))  # type() beépített függvény a változó típusát "adja vissza"

    # 1.2 Numerikus adattípusok: int, float és a literálok
    egesz: int = 68  # Egész érték tárolásához
    valos: float = 3.14  # Valós érték tárolásához
    print(type(egesz))
    print(type(valos))

    # 1.3 Logikai adattípus: bool
    logikai: bool = True  # Logikai értéket tárol, értéke csak True vagy False lehet
    print(logikai)

    # 2. Összetett adattípusok vagy kollekciók: Több érték tárolását teszik lehetővé
    # 2.1 Lista (list, egydimenziós tömb, vagy vektor más programozási nyelveken)
    lista: list[str] = ['apple', 'banana', 'cherry']
    print(lista)

    # 2.2 Tuple (tuple, konstans listának tekinthető)
    konstans_lista: tuple[str, str, str] = ('apple', 'banana', 'cherry')
    print(konstans_lista)

    # 2.3 Halmaz (set, nem lehetnek azonos értékek)
    halmaz: set[str] = {'apple', 'banana', 'cherry'}
    print(halmaz)

    # 2.4 Szótár (dict, kulcs és érték (értékpárok), kulcs egyedi)
    szotar: dict[str, int] = {"alma": 20, "körte": 23, "barack": 33}
    print(szotar)

    # 2.5 Számsorozat (range, for ciklusokhoz használjuk általában)
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


if __name__ == "__main__":
    main()
