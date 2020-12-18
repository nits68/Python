from typing import List


def tökéletes_szám(szám: int) -> bool:
    osztók_összege: int = 0
    for osztó in range(1, szám):
        if szám % osztó == 0:
            osztók_összege += osztó
    return szám == osztók_összege


def main() -> None:
    # Határozzuk meg és írjuk ki a minta szerint
    # az 1 és 1000 közötti tökéletes számokat!
    # Tökéletes számnak nevezzük azokat a természetes
    # számokat, amelyek megegyeznek az önmaguknál kisebb
    # osztóik összegével.

    print('2. feladat: Tökéletes számok 1-1000 között')

    # tökéletes_számok: List[str] = []
    # for szám in range(1, 1001):
    #     if tökéletes_szám(szám):
    #         tökéletes_számok.append(str(szám))
    # print('; '.join(tökéletes_számok))

    tökéletes_számok: List[str] = []
    for szám in range(1, 1001):
        if tökéletes_szám(szám):
            tökéletes_számok.append(str(szám))
    print(*tökéletes_számok, sep='; ')


if __name__ == "__main__":
    main()
