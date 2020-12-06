# Határozza meg két egész szám legnagyobb közös osztóját a következő
# algoritmussal: Mindaddig kisebbítse a nagyobb számot a kisebb számmal,
# amíg a két szám egyenlő nem lesz! Az így kapott szám lesz a
# legnagyobb közös osztó.
# A számok bekérését és az eredmény kiírását a minta szerint végezze!

# Egy lehetséges megoldás:

def main() -> None:
    print('LNKO kivonásos algoritmussal')
    a: int = int(input('a = '))
    b: int = int(input('b = '))
    print(f'LNKO({a},{b}) = ', end='')
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    print(a)


if __name__ == "__main__":
    main()
