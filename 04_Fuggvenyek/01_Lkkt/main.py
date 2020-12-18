import random
#  from random import *  # közvetlenül tudunk a random osztály metódusaira hivatkozni


def lkkt(a: int, b: int) -> int:
    # ksz: int = min(a, b)
    # nsz: int = max(a, b)
    if a > b:
        nsz: int = a
        ksz: int = b
    else:
        nsz: int = b
        ksz: int = a
    osztandó: int = nsz  # nagyobb szám első többszöröse
    while osztandó % ksz != 0:
        osztandó += nsz  # nagyobb szám következő többszöröse
    return osztandó


def main():
    print("\n\nLKKT függvény hívása véletlen számokkal")
    a: int = random.randint(1, 999)
    b: int = random.randint(1, 999)
    print(f'LKKT({a},{b}) = {lkkt(a, b)}')
    print(f'A két szám szorzata: {a} * {b} = {a * b}')


if __name__ == '__main__':
    main()
