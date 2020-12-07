from Eredmeny import Eredmeny
from typing import List


def main() -> None:
    # 1. Olvassa be az ub2017egyeni.txt állományban lévő adatokat és tárolja el
    # egy saját osztály típusú listában!
    # Ügyeljen arram, hogy az állomány első sora a mezőneveket tartalmazza.

    fe: List[Eredmeny] = []
    with open('ub2017egyeni.txt', 'r', encoding='UTF-8') as file:
        for sor in file.read().splitlines()[1:]:
            fe.append(Eredmeny(sor))

    # 2. Határozza meg és írja ki a minta szerint a képernyőre
    # a versenyen elindult futók számát!
    # Minta: 2. feladat: Futók száma: 186

    print(f'2. feladat: Futók száma: {len(fe)}')

    # 3. Számolja meg és írja ki a képernyőre a minta szerint,
    # hogy hány női sportoló teljesítette a teljes távot!
    fo: int = 0
    for f in fe:
        if f.Kategoria == 'Noi' and f.TavSzazalek == 100:
            fo += 1
    print(f'3. feladat: Célba érkező női sportolók: {fo} fő')

    # 4. feladat: Határozzuk meg a leghosszabb nevű futót és és írjuk ki az adatait!
    # Holtverseny esetén csak a futok neveit írjuk egymás mellé!
    print('4. feladat: A leghosszabb nevű futó(k)')
    max_nevhossz_eredmeny: Eredmeny = fe[0]
    for f in fe[1:]:
        if len(f.Nev) > len(max_nevhossz_eredmeny.Nev):
            max_nevhossz_eredmeny = f
    max_nevhossz_futo_db: int = 0
    for f in fe:
        if len(f.Nev) == len(max_nevhossz_eredmeny.Nev):
            max_nevhossz_futo_db += 1
    if max_nevhossz_futo_db == 1:
        print(f'\tNév: {max_nevhossz_eredmeny.Nev}')
        print(f'\tRajtszám: {max_nevhossz_eredmeny.Rajtszam}')
        print(f'\tEredmény: {max_nevhossz_eredmeny.Veresenyido}')
    else:
        print('\tNevek: ', end='')
        for f in fe:
            if len(f.Nev) == len(max_nevhossz_eredmeny.Nev):
                print(f'{f.Nev}', end='; ')
        print()  # soremelés az utolsó futó neve után

    # 4. feladat alternatív megoldása
    max: int = 0
    for f in fe:
        if f.nev_hossz() > max:
            max = f.nev_hossz()
    max_fe: List[Eredmeny] = []
    for f in fe:
        if f.nev_hossz() == max:
            max_fe.append(f)
    if len(max_fe) == 1:
        print(f'\tNév: {max_nevhossz_eredmeny.Nev}')
        print(f'\tRajtszám: {max_nevhossz_eredmeny.Rajtszam}')
        print(f'\tEredmény: {max_nevhossz_eredmeny.Veresenyido}')
    else:
        print('\tNevek: ', end='')
        for f in max_fe:
            print(f'{f.Nev}', end='; ')
        print()  # soremelés az utolsó futó neve után

    # 5. Határozza meg és írja ki a minta szerint a teljes távot teljesítő
    # férfi sportolók átlagos idejét órában!
    # Feltételezheti, hogy legalább egy ilyen sportoló volt.
    osszeg_ido: float = 0
    fo_ff_100: int = 0
    for f in fe:
        if f.Kategoria == 'Ferfi' and f.TavSzazalek == 100:
            fo_ff_100 += 1
            osszeg_ido += f.verseny_ido_ora()
    print(f'5. Férfi sportolók átlagos ideje: {osszeg_ido / fo_ff_100} óra')


if __name__ == "__main__":
    main()
