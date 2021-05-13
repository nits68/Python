import math  # A gyökvonáshoz kell a math modul


def prime_favágó(szám: int) -> bool:
    osztók_száma: int = 0
    for osztó in range(1, szám + 1):
        if szám % osztó == 0:
            # osztók_száma = osztók_száma + 1
            osztók_száma += 1
    return osztók_száma == 2


def prime(szam: int) -> bool:
    if szam > 2 and szam % 2 == 0 or szam == 1:  # A 2-nél nagyobb páros számok és az 1 nem prím!
        return False
    szam_gyoke: int = int(math.sqrt(szam))  # A vizsgálatot a szám gyökéig elegendő végezni
    for oszto in range(3, szam_gyoke + 1, 2):
        if szam % oszto == 0:  # Ha találunk osztót a szám gyöke előtt, akkor a szám nem prím
            return False
    return True


def main():
    print("Prímszám vizsgálat")
    n: int = int(input("n="))
    if prime(n):
        print("A szám prím!")
    else:
        print("A szám nem prím!")

    print("Prímek 1-100 között")
    for i in range(1, 101):
        if prime_favágó(i):
            print(i, end=' ')
    print()


if __name__ == '__main__':
    main()
