#  Kérjen be három (egész|valós) típusú számot és tárolja el, majd
#  írja ki, hogy melyik a nagyobb, melyik a kisebb és melyik a "középső" szám!
#  Feltételezheti, hogy a három szám nem egyenlő!

def main() -> None:
    print('1. feladat: Kisebb-nagyobb-középső meghatározása')
    a: float = float(input('a = '))
    b: float = float(input('a = '))
    c: float = float(input('a = '))
    kisebb: float = min(a, b, c)
    nagyobb: float = max(a, b, c)
    középső: float = a  # feltételezés
    if b != kisebb and b != nagyobb:
        középső = b
    if c != kisebb and c != nagyobb:
        középső = c
    print(f'A kisebb szám: {kisebb}')
    print(f'A középső szám: {középső}')
    print(f'A nagyobb szám: {nagyobb}')


if __name__ == "__main__":
    main()
