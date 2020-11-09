import math


# Másodfokú egyenlet gyökei (folyamatábrát (PDF) követve):
print('Másodfokú egyenlet (a*x*x + b*x + c = 0) gyöke')
print('Kérem az együtthatókat')
a = float(input('a= '))
b = float(input('b= '))
c = float(input('c= '))
if a != 0:
    if math.pow(b, 2) >= 4 * a * c:
        if math.pow(b, 2) > 4 * a * c:
            # Két valós gyök
            # Diszkrimináns (D = b*b-4ac)  > 0
            print('Két gyök!')
            x1 = (-b + math.sqrt(math.pow(b, 2) - 4 * a * c)) / (2 * a)
            x2 = (-b - math.sqrt(math.pow(b, 2) - 4 * a * c)) / (2 * a)
            print(f'x1 = {x1}')
            print(f'x2 = {x2}')
        else:
            # Egy valós gyök
            # Diszkrimináns == 0
            print('Egy gyök!')
            x = -b / (2 * a)
            print(f'x = {x}')
    else:
        # Diszkrimináns < 0
        print('Nincs valós gyök!')
else:
    print('Nem másodfokú!')
    if b != 0:
        x = -b / c
        print(f'x = {x}')
    else:
        if c != 0:
            print('Ellentmondás!')
        else:
            print('Azonosság!')
