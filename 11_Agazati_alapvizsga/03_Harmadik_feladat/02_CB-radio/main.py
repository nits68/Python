from CBadas import CBadas
# from typing import List # Python 3.8.X, vagy alatta kell


def main() -> None:
    print('CB-Rádió')
    # 1. feladat: Olvassa be és tárolja el a cb.txt UTF-8 kódolású szöveges
    # állományban található adatokat!
    # Az összetartozó adatokat saját osztály definiálásával kezelje!
    # A fájl soraiban található adatokat saját osztály típusú listában tárolja!
    # Ügyeljen rá, hogy az állomány első sora a mezőneveket tartalmazza!

    # adasok: List[CBadas] = [] # Python 3.8.X, vagy alatta
    adasok: list[CBadas] = []
    with open('cb.txt', 'r', encoding='utf-8') as file:
        for sor in file.read().splitlines()[1:]:
            # aktAdas: CBadas = CBadas(sor)
            # adasok.append(aktAdas)
            # vagy:
            adasok.append(CBadas(sor))

    # 2. feladat: Határozza meg és írja ki a képernyőre a minta szerint,
    # hogy hány bejegyzés található a forrásállományban!

    # Minta: 2. feladat: Bejegyzések száma: 381 db

    print(f'2. feladat: Bejegyzések száma: {len(adasok)} db')

    # 3. feladat: Határozza meg, hogy 'Sanyi' nevével hány bejegyzés van a forrásállományban!

    # Minta: 3. feladat: Sanyihoz tartozó bejegyzések: 31 db

    sanyi_db: int = 0
    for adas in adasok:
        if adas.nev == 'Sanyi':
            sanyi_db += 1
    print(f'3. feladat: Sanyihoz tartozó bejegyzések: {sanyi_db} db')

    # 4. feladat: Melyik sofőrhöz fűződik az egy percen belüli legtöbb adás?
    # Jelenítse meg az adatsor adatait a képernyőn!
    # Holtverseny esetén az összes adatsor jelenjen meg!

    # Minta:
    # 4. feladat: A legtöbb adás:
    #         Idő: 6:42 Darab: 5 Név: Józsi
    #         Idő: 7:25 Darab: 5 Név: Zoli
    #         Idő: 7:43 Darab: 5 Név: Gabi

    max_adas_darab: int = adasok[0].adas_db
    for adas in adasok[1:]:
        if adas.adas_db > max_adas_darab:
            max_adas_darab = adas.adas_db
    print('4. feladat: A legtöbb adás:')
    for adas in adasok:
        if (adas.adas_db == max_adas_darab):
            print(f'\tIdő: {adas.ora}:{adas.perc} Darab: {adas.adas_db} Név: {adas.nev}')

    # 5. feladat: Készítsen atszamol_percre azonosítóval egész típusú értékkel visszatérő metódust
    # a saját osztályban, ami a az óra- és percértéket percekre számolja át!
    # Egy óra 60 percből áll. Például: 8 óra 5 perc esetén a visszatérési érték: 485 (perc).
    # Készítsen szöveges állományt cb2.txt néven, melybe a forrásállományban található
    # bejegyzéseket írja ki új formátumban! Az órákat és a perceket percekre számolja át az
    # elkészített metódus hívásával! Az új állomány első sorát és az adatsorokat a minta szerint alakítsa ki!

    # Minta cb2.txt:
    # Kezdes;Nev;AdasDb
    # 360;Laci;2
    # 361;Bandi;3
    # ...

    print('5. feladat: cb2.txt állomány létrehozása')
    with open('cb2.txt', 'w', encoding='utf-8') as file:
        file.write('Kezdes;Nev;AdasDb\n')  # fejlécsor kiírása
        for adas in adasok:
            file.write(f'{adas.atszamol_percre()};{adas.nev};{adas.adas_db}\n')


if __name__ == "__main__":
    main()
