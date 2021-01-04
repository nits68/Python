from FilmBemutató import FilmBemutató
from typing import List


def main() -> None:
    # 3.1 Olvassa be az UTF-8 kódolású  nyitohetvege.txt állományban lévő adatokat
    # és tárolja el egy saját osztály típusú listában!
    # Ügyeljen rá, hogy az állomány első sora az adatok fejlécét tartalmazza!
    fb: List[FilmBemutató] = []
    with open('nyitohetvege.txt', 'r', encoding='utf-8') as sr:
        for sor in sr.read().splitlines()[1:]:
            fb.append(FilmBemutató(sor))

    # 3.2 Határozza meg és írja ki a képernyőre a minta szerint,
    # hogy hány filmbemutató található az állományban!
    print(f'3.2 feladat: Filmbemutatók száma: {len(fb)} db')

    # 3.3  Összesítse és írja ki a képernyőre a UIP Duna Film forgalmazó
    # (forgalmazó="UIP") első hetes bevételeinek összegét!
    # Az összeg ezres szeparátorral jelenjen meg a minta szerint!
    összeg_UIP: int = 0
    for film in fb:
        if film.fogalmazó == 'UIP':
            összeg_UIP += film.bevétel
    ki_összeg_e_szep: str = f'{összeg_UIP:,} Ft'  # Egyszerűen csak vesszőt tud a Python szeparátorként
    ki_összeg_e_szep = ki_összeg_e_szep.replace(',', ' ')  # Lecseréljük a vesszőket szóközökre
    print(f'3.3 feladat: UIP összes bevétele az 1. héten: {ki_összeg_e_szep}')

    # 3.4  Határozzuk meg az átlagos nézőszámot az InterCom által forgalmazott
    # filmek esetében! Feltételezheti, hogy legalább 1 filmet forgalmazott a cég.
    # Az átlagot a minta szerint 1 tizedesjegyre kerekítve jelenítse meg!
    össz_néző_intercom: int = 0
    db_intercom: int = 0
    for film in fb:
        if film.fogalmazó == 'InterCom':
            össz_néző_intercom += film.látogató
            db_intercom += 1
    print(f'3.4 feladat: Átlagos nézőszám InterCom: {össz_néző_intercom / db_intercom:.1f} fő')

    # 3.5 Döntse el, hogy az adatok között található-e 2018-ban bemutatott film!
    # A keresését ne folytassa, ha a választ meg tudja adni!
    # A képernyőre írást a minta szerint végezze!
    volt_2018as_film: bool = False
    for film in fb:
        if film.bemutató >= '2018.01.01' and film.bemutató <= '2018.12.31':
            volt_2018as_film = True
            break
    print(f'3.5 feladat: Volt 2018-as bemutató? {"Igen" if volt_2018as_film else "Nem"}')


if __name__ == "__main__":
    main()
