import math  # A gyökvonáshoz kell a math osztály


def prime(szam: int) -> bool:
    if szam > 2 and szam % 2 == 0 or szam == 1:  # A 2-nél nagyobb páros számok és az 1 nem prím!
        return False
    szam_gyoke: int = int(math.sqrt(szam))  # A vizsgálatot a szám gyökéig elegendő végezni
    for oszto in range(3, szam_gyoke + 1, 2):
        if szam % oszto == 0:  # Ha találunk osztót a szám gyöke előtt, akkor az szám nem prím
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
        if prime(i):
            print(i, end=' ')


if __name__ == '__main__':
    main()
