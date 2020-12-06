import math


def main() -> None:
    # Másodfokú egyenlet gyökei (folyamatábrát (MFEGY_feladat.pdf) követve):
    print('Másodfokú egyenlet (a*x*x + b*x + c = 0) gyöke')
    print('Kérem az együtthatókat')
    a: float = float(input('a= '))
    b: float = float(input('b= '))
    c: float = float(input('c= '))
    if a != 0:
        if math.pow(b, 2) >= 4 * a * c:
            if math.pow(b, 2) > 4 * a * c:
                # Két valós gyök
                # Diszkrimináns (D = b*b-4ac)  > 0
                print('Két gyök!')
                x1: float = (-b + math.sqrt(math.pow(b, 2) - 4 * a * c)) / (2 * a)
                x2: float = (-b - math.sqrt(math.pow(b, 2) - 4 * a * c)) / (2 * a)
                print(f'x1 = {x1}')
                print(f'x2 = {x2}')
            else:
                # Egy valós gyök
                # Diszkrimináns == 0
                print('Egy gyök!')
                x: float = -b / (2 * a)
                print(f'x = {x}')
        else:
            # Diszkrimináns < 0
            print('Nincs valós gyök!')
    else:
        print('Nem másodfokú!')
        if b != 0:
            x: float = -b / c
            print(f'x = {x}')
        else:
            if c != 0:
                print('Ellentmondás!')
            else:
                print('Azonosság!')


if __name__ == "__main__":
    main()
