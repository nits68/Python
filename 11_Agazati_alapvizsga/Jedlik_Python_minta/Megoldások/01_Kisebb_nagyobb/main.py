def main() -> None:
    print('1. feladat: Kisebb-nagyobb meghatározása')
    a: int = int(input('Kérem az első számot: '))
    b: int = int(input('Kérem a második számot: '))

    if a > b:
        print(f'A nagyobb szám {a}, a kisebb {b}.')
    elif b > a:
        print(f'A nagyobb szám {b}, a kisebb {a}.')
    else:
        print('A két szám egyenlő.')

    # Alternatív megoldás a max() és min() függvényekkel:

    # if a == b:
    #     print('A két szám egyenlő.')
    # else:
    #     print(f'A nagyobb szám {max(a,b)}, a kisebb {min(a,b)}.')


if __name__ == "__main__":
    main()
