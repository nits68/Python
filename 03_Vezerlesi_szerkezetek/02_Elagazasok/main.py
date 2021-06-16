import random


def main() -> None:
    # Szelekciók (elágazások): Olyan vezérlési szerkezetek, ahol feltétel(ek)hez kötjük az utasítások végrehajtását

    # Elágazások fajtái:
    # - egy ágú (if)
    # - kétágú (if-else)
    # - többágú (if-elif-elif- ... -elif-else) (switch-case szerkezet nincs a Python-ban)

    # Példa egyágú (if) szelekcióra:
    print('Szám abszolút értéke')
    inputX: int = int(input('x= '))
    absX: int = inputX
    if inputX < 0:
        # absX = -inputX  # Előjelváltás
        absX = inputX * -1
    print(f'Abs({inputX}) = {absX}')

    # Példa kétágú (if-else) elágazásra
    print('\nPáros-páratlan meghatározása')
    inputSzám: int = int(input('szam= '))
    if inputSzám % 2 == 0:
        print('A szám páros!')
    else:
        print('A szám páratlan!')

    # Példa többágú (if-elif-else) elágazásra (else "ág" elhagyható):
    print('\nOsztályzat szöveges megfelelője')
    érdemjegy: int = int(input('Kérem az osztályzatot [1-5]: '))
    if érdemjegy == 1:
        print('Elégtelen')
    elif érdemjegy == 2:
        print('Elégséges')
    elif érdemjegy == 3:
        print('Közepes')
    elif érdemjegy == 4:
        print('Jó')
    elif érdemjegy == 5:
        print('Jeles')
    else:  # Az else ág opcionális, azaz elhagyható
        print('Ez nem osztályzat!')

    # Rövidített (shorthand) kétágú elágazás, amit feltételes operátor funkcióját is betöltheti:
    # Véletlen egész számok generálása a random osztály (modul) randint() függvényével:
    # Használat elött a random modult importálni kell: import random
    a: int = random.randint(10, 20)
    b: int = random.randint(10, 20)
    print("A") if a > b else print("B")
    c: int = 12 if a != b else 24
    # A fenti értékadás C# feltételes operátorral:
    # c = a != b ? 12 : 24
    print(c)  # 12

    # A pass utasítást akkor használjuk, ha később szeretnék egy igaz-hamis ág (blokk) utastásait megadni,
    # de kerülni szeretnénk a szintaktikai hibákat
    if b > a:
        pass
    else:
        pass


if __name__ == "__main__":
    main()
