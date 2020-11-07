from typing import Set


def main():
    #  Halmaz (Set) létrehozása:
    halmaz1: Set[str] = {'barack', 'körte', 'szilva', 'alma', 'szőlő'}  # Elemekkel inicializált halmaz
    halmaz2 = {}   # Üres halmaz
    halmaz3 = set((1, 2, "a"))  # set() konstruktorral tuple-ból létrehozott halmaz
    halmaz4 = set(['a', 'e', 'i', 'o', 'u'])  # set() konstruktorral listából létrehozott halmaz

    # Teljes lista kiírása
    print(halmaz1)
    print(halmaz2)
    print(halmaz3)
    print(halmaz4)

    # Tartalmazás vizsgálat az IN operátorral
    if 'alma' in halmaz1:
        print('Az alma érték megtalálható a halmazban!')

    # Halmaz elemeinek módosítása:
    # Csak elem hozzáadására, törlésére van lehetőség

    # Egy elem hozzáadása: add()
    halmaz1.add('szilva')  # Mivel már létezik, nem fog növekedni a halmaz elemszáma, nincs hibaüzenet
    print(halmaz1)
    halmaz1.add('répa')
    print(halmaz1)

    # Több elem hozzáadása: update()
    halmaz1.update({'zeller', 'karalábé', 'karfiol'})  # Paraméter lehet lista, halmaz, stb.
    print(halmaz1)

    # Halmaz elemszáma: len()
    print(f'A halmaz1 elemszáma: {len(halmaz1)}')

    # Elem törlése: remove() vagy discard()
    halmaz1.discard('zeller')
    halmaz1.discard('zeller')  # Ha az elem nem létezik, akkor nem dob hibát a discard()
    try:
        halmaz1.remove('karfiol')
        halmaz1.remove('karfiol')  # A remove() hibát dob, ha az elem nem létezik
    except Exception as ex:
        print(ex.__doc__)
    print(halmaz1)

    # Egy elem törlése: pop(), ne használjuk, mert nem tudjuk, hogy melyik elemet fogja törölni
    print(halmaz1.pop())
    print(halmaz1)

    # Halmaz bejárása
    for i in halmaz1:
        print(f'{i} ', end='')
    print()  # Soremelés

    # Halmaz ürítése: clear()
    halmaz1.clear()
    print(halmaz1)

    # Halmaz teljes törlése: del
    del halmaz1

    # Halmazok uniója: union()
    h1 = {"a", "b", "c"}
    h2 = {"b", "c", "d"}
    h3 = h1.union(h2)
    print(h3)

    # Halmazok metszete: intersection()
    h1 = {"a", "b", "c"}
    h2 = {"b", "c", "d"}
    h3 = h1.intersection(h2)
    print(h3)

    # Halmazok különbsége: difference()
    h1 = {"a", "b", "c"}
    h2 = {"b", "c", "d"}
    h3 = h1.difference(h2)
    print(h3)

    # Érdekes lehet még:
    # isdisjoint() -->	Returns whether two sets have a intersection or not
    # issubset() --> Returns whether another set contains this set or not
    # copy() --> Returns a copy of the set


if __name__ == '__main__':
    main()
