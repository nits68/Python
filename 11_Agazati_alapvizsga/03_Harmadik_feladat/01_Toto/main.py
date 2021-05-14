from fogadasi_fordulo import Fogadasi_fordulo
# from typing import List # Python 3.8.X, vagy alatta kell


def main() -> None:
    # 1. feladat: Olvassa be és tárolja el a toto.txt UTF-8 kódolású szöveges
    # állományban található adatokat!
    # Az összetartozó adatokat saját osztály definiálásával kezelje!
    # A fogadási fordulók adatait saját osztály típusú listában tárolja!
    # Ügyeljen rá, hogy az állomány első sora a mezőneveket tartalmazza.

    print('Toto feladat')
    print('1. feladat: Adatok beolvasása és tárolása')
    # ff: List[Fogadasi_fordulo] = []  #  Python 3.8.X, vagy alatta
    ff: list[Fogadasi_fordulo] = []
    with open('toto.txt', 'r', encoding='UTF-8') as file:
        for sor in file.read().splitlines()[1:]:
            ff.append(Fogadasi_fordulo(sor))

    # 2. feladat: Határozza meg és írja ki a fogadási fordulók számát

    # Minta: 2. feladat: Fogadási fordulók száma: 1630

    print(f'2. feladat: Fogadási fordulók száma: {len(ff)}')

    # 3. feladat: Számolja meg és írja ki a képernyőre a telitalálatos szelvények számát!

    # Minta: 3. feladat: Telitalálatos szelvények száma: 13718 darab

    szelveny13p1_darab: int = 0
    for e in ff:
        szelveny13p1_darab += e.t13p1
    print(f'3. feladat: Telitalálatos szelvények száma: {szelveny13p1_darab} darab')

    # 4. feladat: Döntse el, hogy volt-e olyan forduló, ahol nem volt döntetlen mérkőzés

    # Minta: 4. feladat: Volt döntetlen mentes forduló!

    volt_ilyen_fordulo: bool = False
    for e in ff:
        if e.nem_volt_dontetlen():
            volt_ilyen_fordulo = True
            break
        # vagy:
        # if e.eredmenyek.count('X') == 0:
        #     volt_ilyen_fordulo = True
        #     break

    print(f'4. feladat: {"Volt" if volt_ilyen_fordulo else "Nem volt"} döntetlen mentes forduló!')


if __name__ == "__main__":
    main()
