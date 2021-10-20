# Kérjen be a, b, c valós típusú változóba értékeket!
# Ezek az értékek lesznek az ax2 + bx + c = 0 másodfokú egyenlet együtthatói.
# Készítsen függvényt, ami meghatározza az együtthatók alapján
# a másodfokú egyenlet gyökeinek a számát!
# D = b2 - 4ac
# D > 0 -> 2 gyök
# D == 0 -> 1 gyök
# D < 0 -> 0 gyök
# A függvény -1-es értékkel térjen vissza, ha az egyenlet nem másodfokú!
# Az input együtthatókkal hívja a függvényt és állapaitsa meg a gyökök számát a
# kiadott minták szerint!

# Minták:

# Másodfokú egyenlet gyökeinek a száma
# Kérem az együtthatókat
# a = 0
# b = 1
# c = 2
# Az egyenlet nem másodfokú!

# Másodfokú egyenlet gyökeinek a száma
# Kérem az együtthatókat
# a = 1
# b = 2
# c = 1
# Megoldások száma: 1db

# Másodfokú egyenlet gyökeinek a száma
# Kérem az együtthatókat
# a = 12
# b = 3456
# c = 78
# Megoldások száma: 2db

import math


def mfe_gyökök_száma(a: float, b: float, c: float) -> int:
    if a == 0:
        return -1
    diszkrimináns: float = math.pow(b, 2) - 4 * a * c
    gyökök_száma: int = 0
    if diszkrimináns == 0:
        return 1
    elif diszkrimináns > 0:
        return 2
    return gyökök_száma


def main() -> None:
    print('Másodfokú egyenlet gyökeinek a száma')
    print('Kérem az együtthatókat')
    a: float = float(input('a = '))
    b: float = float(input('b = '))
    c: float = float(input('c = '))

    gysz: int = mfe_gyökök_száma(a, b, c)

    if gysz == -1:
        print('Az egyenlet nem másodfokú!')
    else:
        print(f'Megoldások száma: {gysz}db')


if __name__ == "__main__":
    main()
