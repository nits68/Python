import random


def main() -> None:
    # 1 Összetett adatszerkezet feltöltésének módjai

    # 1.1 Feltöltés felhasználói input útján (időigényes):
    # nevek: list[str] = []
    # print('Kérem a neveket 0-végjelig!')
    # inputNév: str = ''
    # while inputNév != '0':
    #     inputNév = input('Név: ')
    #     if inputNév != '0' and len(inputNév) != 0:
    #         nevek.append(inputNév)
    # print(nevek)

    # 1.2 Feltöltés véletlen értékekkel:
    számok: list[int] = []
    for i in range(5):
        számok.append(random.randint(10, 99))

    # 1.3 Feltöltés literálokkal:
    állítások: list[bool] = [True, True, False, True, False]
    print(állítások)

    # 1.4 Feltöltés szöveges állományból (sorokként csak egy adat van):
    with open('bukk-videk.txt', 'r', encoding='UTF-8') as sr:
        sorok: list[str] = sr.read().splitlines()
    magasságok: list[float] = []
    for sor in sorok:
        magasságok.append(float(sor))
    print(magasságok[:10])
    del sorok

    # 2 Összetett adatszerkezet bejárása
    # Vizsgálathoz, műveletekhez rendre "elővesszük" az összetett adatszerkezet elemeit
    # 2.1 Nincs szükség az elem indexére
    for e in számok:
        print(e, end=' ')
    print()

    # 2.2 Értékek (számok[i]) és indexek (i) rendelkezésre állnak
    for i in range(len(számok)):
        print(f'számok[{i}] = {számok[i]} ')

    # Vagy: Értékek (e) és indexek (i) rendelkezésre állnak
    for i, e in enumerate(számok):
        print(f'számok[{i}] = {e}', end=' ')
    print()

    # 3 Egy sorozathoz egy értéket rendelő programozási tételek
    # 3.1 Eldöntés tétele: Megadott tulajdonságú érték megtalálható-e a listában?
    # Feladat: Döntse el, hogy található-e páratlan szám a listában!
    # A keresést ne folytassa, ha a választ megtudja adni!

    vanPáratlan: bool = False  # Feltételezzük, hogy nincsen páratlan szám a listában
    for szám in számok:
        if szám % 2 == 1:
            vanPáratlan = True
            break
    # Kiírás lehetőségei
    if vanPáratlan:
        print('A listában van páratlan szám!')
    else:
        print('A listában nincs páratlan szám!')
    # vagy:
    print('A listában ' + 'van' if vanPáratlan else 'nincs' + ' páratlan szám!')
    # vagy:
    print(f'A listában {"van" if vanPáratlan else "nincs"} páratlan szám!')

    # 3.2 Megszámlálás tétele: Megadott tulajdonságú értékek darabszáma
    # Feladat: Határozzuk meg az ötvennél nagyobb páros számok darabszámát!
    db_páros_50: int = 0
    for e in számok:
        if e % 2 == 0 and e > 50:
            db_páros_50 += 1
    print(f'Ötvennél nagyobb páros számok darabszáma: {db_páros_50}')

    # 3.3 Összegzés tétele: Megadott tulajdonságú értékek összege/átlaga
    # Feladat: Határozzuk meg az 5-el osztható számok átlagát!
    db_oszt5: int = 0
    összeg_oszt5 = 0
    for e in számok:
        if e % 5 == 0:
            db_oszt5 += 1
            összeg_oszt5 += e
    if db_oszt5 == 0:
        print('Nincs a listában 5-el osztható szám!')
    else:
        print(f'Az 5-el osztható számok darabszáma: {db_oszt5}')
        print(f'Az összegük: {összeg_oszt5} és az átlaguk: {összeg_oszt5 / db_oszt5}')

    # 3.4 Szélsőérték (minimum, maximum) keresése
    # 3.4.1 Csak a legnagyobb elem értékét kell meghatározni:
    # Feladat: Határozzuk meg a legnagyobb elem/elemek értékét!
    max: int = számok[0]  # Kinevezzük az első elemet a legnagyobbnak
    for szám in számok[1:]:  # számok[1:] -> Az első elemet elhagyjuk, önmagához nem hasonlítjuk
        if szám > max:
            max = szám
    print(f'A legnagyobb szám értéke: {max}')

    # 3.4.2 A legnagyobb elem értéke és az indexe is kell:
    # Feladat: Határozzuk meg a legkisebb elem értékét és indexét!
    # Holtverseny esetén elegendő az elsőt megadnia.
    mini: int = 0  # Kinevezzük az első elemet a legkisebbnek
    for i in range(1, len(számok)):
        if számok[i] < számok[mini]:
            mini = i
    print(f'A legkisebb szám értéke: {számok[mini]}, indexe: {mini}')

    # 3.4.3 A holtversenyt is kezelni kell
    # Feladat: Holtverseny esetén írjuk ki az összes elem indexét
    print('Legkisebb elem(ek) indexei:', end=' ')
    for i, e in enumerate(számok):
        if (e == számok[mini]):
            print(i, end=' ')
    print()

    # 3.4.4 Nem nevezhető ki az első elem a legkisebb/legnagyobb elemnek
    # Feladat: Határozzuk meg a legnagyobb páratlan szám értékét és indexét a listában!
    maxi_páratlan: int = -1  # Ha -1 marad az értéke, akkor nincs páratlan szám a listában
    for i, e in enumerate(számok):
        if e % 2 == 1:  # Ha páratlan
            if maxi_páratlan == -1:  # Első páratlan szám a listában
                maxi_páratlan = i  # Kinevezzük a legnagyobb páratlan számnak
            else:
                if e > számok[maxi_páratlan]:
                    maxi_páratlan = i
    if maxi_páratlan == -1:
        print('Nincs a listában páratlan szám!')
    else:
        print(f'A legnagyobb páratlan szám értéke: {számok[maxi_páratlan]}, indexe: {maxi_páratlan}')

    # 4 Egy sorozathoz egy sorozatot rendelő programozási tételek
    # 4.1 Kiválogatás
    # Feladat: Válogassuk ki a 3-al osztható számokat!
    osztható3al: list[int] = []
    for e in számok:
        if e % 3 == 0:
            osztható3al.append(e)
    print(f'A 3-al osztható számok: {osztható3al}')

    # 4.2 Rendezés
    # Feladat: Rendezzük a lista elemeit a buborékos rendezés algoritmusával!
    for ig in range(len(számok) - 1, 0, -1):  # ig -> 9..1 (10 elemű lista esetén)
        csere_volt: bool = False
        for i in range(ig):  # i -> 0..8 / 0..7 / 0..6 / ... / 0..0/  (10 elemű lista esetén)
            if (számok[i] > számok[i+1]):  # Cserélni kell az egymás mellett álló elemeket
                seged: int = számok[i]  # segédváltozó két érték felcseréléséhez
                számok[i] = számok[i+1]
                számok[i+1] = seged
                csere_volt = True
        if csere_volt is False:  # Ha nem volt csere, akkor rendezett a lista, kiléphetünk
            break
    print(f'Rendezve: {számok}')

    # 5 Egy sorozathoz két sorozatot rendelő programozási tételek
    # 5.1 Szétválogatás
    # Válogassuk szét a páros és páratlan számokat!
    páros_számok: list[int] = []
    páratlan_számok: list[int] = []
    for e in számok:
        if e % 2 == 0:
            páros_számok.append(e)
        else:
            páratlan_számok.append(e)
    print(f'A páros lista: {páros_számok}')
    print(f'A páratlan lista: {páratlan_számok}')

    # 6 Két sorozathoz egy sorozatot rendelő programozási tételek
    # 6.1 Összefuttatás (rendezettek uniója)
    # 6.2 Egyesítés (unió)
    # 6.3 Metszet


if __name__ == "__main__":
    main()
