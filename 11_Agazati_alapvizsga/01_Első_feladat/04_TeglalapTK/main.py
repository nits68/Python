# Kérje be egy téglalap oldalait és tárolja őket valós|egész típusú változókba,
# majd határozza meg, a téglalap területét és kerületét!
# A területet és a kerületet a következő képletekkel számolja:
# T = a * b
# K = 2 * (a + b)

# Egy lehetséges megoldás:

def main() -> None:
    print('Téglalap kerülete és területe')
    print('Adja meg a téglalap oldalait!')
    a: float = float(input('a= '))
    b: float = float(input('b= '))
    terulet: float = a * b
    kerulet: float = 2 * (a + b)
    print(f'T = {terulet}')
    print(f'K = {kerulet}')


if __name__ == "__main__":
    main()
