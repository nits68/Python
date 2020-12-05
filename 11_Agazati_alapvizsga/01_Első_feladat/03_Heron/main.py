# Kérje be és tárolja el egy háromszög oldalait egész|valós típusú változókba,
# majd határozza meg és írja ki, a háromszög területét és kerületét a Heron képlet segítségével!
# Feltételezheti, hogy az input adatokból háromszög szerkeszthető!
# Heron képlet:
# s = K/2
# T = Gyök(s * (s-a) * (s-b) * (s-c))

# Lehetséges megoldás:
import math


def main() -> None:
    print('Háromszög kerülete és területe - Heron képlet')
    print('Kérem a háromszög oldalait')
    a: float = float(input('a = '))
    b: float = float(input('b = '))
    c: float = float(input('c = '))
    kerulet: float = a+b+c
    s: float = kerulet / 2
    terulet: float = math.sqrt(s*(s-a)*(s-b)*(s-c))
    print(f'K = {kerulet}')
    print(f'T = {terulet}')


if __name__ == "__main__":
    main()
