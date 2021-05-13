# LKKT - Legkisebb közös többszörös
# Kérjen be két pozitív egész számot és határozza meg a legkisebb
# közös többszörösüket!
# Algoritmus: A felhasználói inputból (a, b) először
# meghatározzuk a nagyobb és kisebb számokat (nsz, ksz).
# Ezután mindaddig növeljük az osztandót a nagyobbik számmal
# (azaz a nagyobbik szám többszöröseit állítjuk elő),
# amíg a kisebbik szám nem osztja az osztandót maradék nélkül.
# Ez az osztandó lesz a két szám legkisebb közös többszöröse.

def main() -> None:
    print('1.feladat: LKKT')
    a: int = int(input('a = '))
    b: int = int(input('b = '))
    nsz: int
    ksz: int

    if a > b:
        nsz = a
        ksz = b
    else:
        nsz = b
        ksz = a

    osztandó: int = nsz

    while osztandó % ksz != 0:
        # osztandó = osztandó + nsz
        osztandó += nsz
    LKKT: int = osztandó
    print(f'LKKT({a},{b}) = {LKKT}')


if __name__ == "__main__":
    main()
