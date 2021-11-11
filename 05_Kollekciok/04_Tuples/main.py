# pylint: disable=line-too-long

def main() -> None:
    #  Tuple létrehozása:
    tuple1: tuple[str, str, str, str, str] = ('barack', 'körte', 'szilva', 'alma', 'szőlő')  # Elemekkel definiált típusos tuple
    tuple2 = ()   # Üres tuple
    tuple3 = tuple((1, 2, 3))  # tuple() osztálykonstruktorral tuple-ból létrehozott tuple
    tuple4 = tuple({'a', 'e', 'i', 'o', 'u'})  # tuple() osztálykonstruktorral halmazból létrehozott tuple
    tuple5 = tuple(['a', 'e', 'i', 'o', 'u'])  # tuple() osztálykonstruktorral listából létrehozott tuple

    # Teljes tuple kiírása
    print(tuple1)  # ('barack', 'körte', 'szilva', 'alma', 'szőlő')
    print(tuple2)  # ()
    print(tuple3)  # (1, 2, 3)
    print(tuple4)  # ('e', 'o', 'u', 'a', 'i')
    print(tuple5)  # ('a', 'e', 'i', 'o', 'u')

    # Hivatkozás tuple elemeire (indexelés)
    # A tuple-k elemit 0-tól indulva egész számokkal indexeljük:
    print(tuple1[0])  # barack
    # indexelés index tartománnyal
    print(tuple1[1:3])  # ('körte', 'szilva')
    print(tuple1[1:])  # ('körte', 'szilva', 'alma', 'szőlő')
    print(tuple1[:2])  # ('barack', 'körte')
    # negatív indexet is használhatunk:
    print(tuple1[-1])  # szőlő
    print(tuple1[-3:-1])  # ('szilva', 'alma')

    # Értékadás nem lehetséges, mivel a tuple-k értékeit nem lehet módosítani
    # megváltoztathatatlan (unchangeable or immutable)
    # tuple1[0] = 'alma'

    # Tuple bejárása index nélkül
    for i in tuple1:
        print(f'{i} ', end='')  # barack körte szilva alma szőlő
    print()  # Soremelés

    # Tuple bejárása indexekkel
    for index, item in enumerate(tuple1):
        print(f'tuple1[{index}]={item} ', end='')  # tuple1[0]=barack tuple1[1]=körte tuple1[2]=szilva ...
    print()  # Soremelés

    # Tartalmazás vizsgálat az IN operátorral
    if 'barack' in tuple1:
        print('A barack érték megtalálható a listában!')

    # A tuple eleminek száma, tuple "hossza": len() függvény
    print(F'A tuple1 lista elemeinek száma: {len(tuple1)}')  # 5

    # Teljes tuple törlése
    del tuple2
    #  print(lista2)  # Hiba: UnboundLocalError: local variable 'tuple2' referenced before assignment

    # Megadott értékű elem darabszáma: count()
    tuple6 = (4, 5, 6, 5, 5, 3, 4, 5, 6)
    print(tuple6.count(5))  # 4

    # Megadott elem első előfordulásának az indexe: index()
    print(tuple6.index(6))  # 2

    # Tuple konvertálása listává, majd vissza
    lista6: list[int] = list(tuple6)
    lista6[1] = 7  # Csak ezzel a trükkel változtatható
    tuple6 = tuple(lista6)
    print(tuple6)  # (4, 7, 6, 5, 5, 3, 4, 5, 6)

    # Tuple-k összeadása
    tuple7 = tuple3 + tuple4
    print(tuple7)  # (1, 2, 3, 'o', 'i', 'a', 'e', 'u')

    # Egy elemű tuple (sok értelme nincs)
    tuple1elemmel = ("apple",)  # Az egy elem után ki kell tenni a vesszőt, hogy tuple legyen
    print(type(tuple1elemmel))  # <class 'tuple'>
    # NOT a tuple
    tuple1elemmel = ("apple")  # Így egyszerű string lesz a típusa
    print(type(tuple1elemmel))  # <class 'str'>


if __name__ == '__main__':
    main()
