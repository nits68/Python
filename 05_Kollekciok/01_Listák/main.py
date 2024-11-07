# pylint: disable=line-too-long
import locale  # magyar nyelvű rendezéshez


def main() -> None:
    # A lista összetett adatszerkezet (kollekció) amely több,
    # különböző típusú adat tárolására alkalmas
    # Mi a listákat úgy fogjuk használni,
    # hogy a lista elemei azonos típusúak lesznek (típusos listák)
    # Más programozási nyelvekben a listákat egydimenziós tömböknek vagy vektoroknak hívjuk
    # Lista létrehozása:
    lista1: list[str] = []  # üres listával inicializált lista
    lista1: list[str] = list()  # list osztálykonstruktorral inicializált lista
    lista1: list[str] = [
        "barack",
        "körte",
        "szilva",
        "alma",
        "szőlő",
    ]  # Elemekkel inicializált lista:
    lista2: list[str] = []
    lista3 = list((1, 2, "a"))  # list() konstruktorral tuple-ból létrehozott lista
    lista4 = list(
        {"a", "e", "i", "o", "u"}
    )  # list() konstruktorral halmazból létrehozott lista
    lista5 = list(
        range(5, 18, 3)
    )  # list() konstruktorral számsorozatból létrehozott lista

    # c# típusú "lista", ami a c# nyelven egydimenziós tömb (vektor)
    # Elemszám: 20, alapértelmezett érték 0
    lista8: list[int] = [0] * 20

    # Teljes lista kiírása
    print(lista1)  # ['barack', 'körte', 'szilva', 'alma', 'szőlő']
    print(lista2)
    print(lista3)
    print(lista4)
    print(lista5)  # [5, 8, 11, 14, 17]
    print(lista8)

    # Hivatkozás lista elemeire (indexelés)
    # Listák elemit 0-tól indulva egész számokkal indexeljük:
    print(lista1[0])  # barack
    # indexelés index tartománnyal
    print(lista1[1:3])  # ['körte', 'szilva']
    print(lista1[1:])  # ['körte', 'szilva', 'alma', 'szőlő']
    print(lista1[:2])  # ['barack', 'körte']
    # negatív indexet is használhatunk:
    print(lista1[-1])  # szőlő
    print(lista1[-3:-1])  # ['szilva', 'alma']

    # Értékadás
    lista1[0] = "alma"
    print(lista1)
    # lista1[0] = True  # A lista elemi bármikor válthatják típusukat,
    # de a Pylance figyelmeztetést dob
    lista1[0] = "True"
    # lista1[1] = 123
    lista1[1] = "123"
    print(lista1)

    # Lista eleminek száma, lista "hossza": len() függvény
    print(f"A lista1 lista elemeinek száma: {len(lista1)}")  # 5

    # Lista bejárása index nélkül
    for e in lista1:
        print(f"{e} ", end="")  # True 123 szilva alma szőlő
    print()  # Soremelés
    # Lista bejárása indexekkel
    for i, e in enumerate(lista1):
        print(f"lista1[{i}]={e} ", end="")  # True 123 szilva alma szőlő
    print()  # Soremelés
    # vagy:
    for i in range(len(lista1)):
        print(f"lista1[{i}]={lista1[i]} ", end="")  # True 123 szilva alma szőlő

    # Tartalmazásvizsgálat az IN operátorral
    if "alma" in lista1:
        print("Az alma érték megtalálható a listában!")
    else:
        print("Az alma érték nem található meg a listában!")

    # Elem hozzáadása a lista végéhez: append()
    lista2.append("hétfő")
    lista2.append("kedd")
    lista2.append("szerda")
    print(lista2)  # ['hétfő', 'kedd', 'szerda']

    # Elem beszúrása a listába: insert()
    lista2.insert(2, "próba")  # A megadott indexű (2) elem elé szúr be
    print(lista2)  # ['hétfő', 'kedd', 'próba', 'szerda']
    # Beszúrás a lista elejére
    lista2.insert(0, "hétfő")
    print(lista2)  # ['hétfő', 'hétfő', 'kedd', 'próba', 'szerda']

    # Megadott értékű elem első előfordulásának törlése: remove()
    lista2.remove("hétfő")
    print(lista2)  # ['hétfő', 'kedd', 'próba', 'szerda']

    # Utolsó elem vagy a megadott indexű elem törlése
    lista2.pop()  # Utolsó elem törlése
    print(lista2)  # ['hétfő', 'kedd', 'próba']
    lista2.pop(1)  # Megadott indexű (1) elem törlése
    print(lista2)  # ['hétfő', 'próba']

    # Lista ürítése (minden elem törlése)
    lista2.clear()
    print(lista2)  # []

    # Teljes lista törlése
    del lista2
    # print(lista2)  # Hiba: UnboundLocalError: local variable 'lista2' referenced before assignment

    # Másolat készítése listából
    # Így nem készül másolat, hanem a lista2 ugyanazon referenciára (memóriacímre) mutat
    lista2 = lista1
    lista2.pop()
    print(lista1)  # [True, 123, 'szilva', 'alma']
    print(lista2)  # [True, 123, 'szilva', 'alma']

    # Másolat 1. módszer: copy()
    lista2 = lista1.copy()
    lista2.pop()
    print(lista1)  # [True, 123, 'szilva', 'alma']
    print(lista2)  # [True, 123, 'szilva']

    # Másolat 2. módszer: list() konstruktorral
    lista5 = list(lista1)
    print(lista5)  # [True, 123, 'szilva', 'alma']

    # Megadott értékű elem darabszáma: count()
    lista6 = [4, 5, 6, 5, 5, 3, 4, 5, 6]
    print(lista6.count(5))  # 4

    # Megadott elem első előfordulásának az indexe: index()
    # Ha az elem nem létezik, akkor "hibát dob"
    print(lista6.index(6))  # 2

    # Lista bővítése másik listával: extend()
    lista_A = ["a", "b", "c"]
    lista_B = ["1", "2", "3"]
    lista_A.extend(lista_B)
    print(lista_A)  # ['a', 'b', 'c', '1', '2', '3']

    # Lista "megfordítása": reverse()
    print(lista6)  # [4, 5, 6, 5, 5, 3, 4, 5, 6]
    lista6.reverse()
    print(lista6)  # [6, 5, 4, 3, 5, 5, 6, 5, 4]

    # Lista rendezése: sort()
    lista6.sort()  # Növekvő sorrend
    print(lista6)  # [3, 4, 4, 5, 5, 5, 5, 6, 6]

    lista6.sort(reverse=True)  # Csökkenő sorrend
    print(lista6)  # [6, 6, 5, 5, 5, 5, 4, 4, 3]

    # Magyar ékezetes karakterláncok rendezése (érdekesen rendez ...):
    lista7: list[str] = [
        "Örs",
        "Éva",
        "Endre",
        "Ödön",
        "Olga",
        "Ádám",
        "Andi",
        "Abigél",
        "Émile",
    ]
    locale.setlocale(locale.LC_ALL, "hu")
    lista7.sort(key=locale.strxfrm)
    print(lista7)


if __name__ == "__main__":
    main()
