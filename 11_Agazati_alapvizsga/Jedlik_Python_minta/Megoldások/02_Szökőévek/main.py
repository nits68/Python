from typing import List


def szökőév(év: int) -> bool:
    return év % 400 == 0 or év % 4 == 0 and év % 100 != 0


def main() -> None:
    print('2. feladat: Szökőév listázó')
    év1: int = int(input('Kérem az egyik évszámot: '))
    év2: int = int(input('Kérem a másik évszámot: '))
    tól_év: int = min(év1, év2)
    ig_év: int = max(év1, év2)
    szökőévek: List[str] = []
    for év in range(tól_év, ig_év + 1):
        if szökőév(év):
            szökőévek.append(str(év))
    if len(szökőévek) == 0:
        print('Nincs szökőév a megadott tartományban!')
    else:
        évek: str = '; '.join(szökőévek)
        print(f'Szökőévek: {évek}')


if __name__ == "__main__":
    main()
