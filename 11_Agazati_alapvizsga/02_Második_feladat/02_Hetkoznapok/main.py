# Feladat: Egy string listát inicializáljon a hétköznapok kisbetűs neveivel!
#    ['hétfő', 'kedd', 'szerda', 'csütörtök', 'péntek']
# Készítsen függvényt, ami a paraméterében átadott nap nevében
# meghatározza a magyar magánhangzók (aáeéiíoóöőuúüű) számát!
# A saját függvény felhasználásával írja ki,
# hogy melyik hétköznap nevében van a legtöbb magánhangzó!

# Minta: A legtöbb magánhangzó a csütörtök-ben van!

# Egy lehetséges megoldás:
from typing import List


def maganhangzok_szama(nap: str) -> int:
    db: int = 0
    for karakter in nap:
        if karakter in 'aáeéiíoóöőuúüű':
            db += 1
    return db


napok: List[str] = ['hétfő', 'kedd', 'szerda', 'csütörtök', 'péntek']
maxi_mgh: int = 0
for i in range(1, len(napok)):
    print(maganhangzok_szama(napok[i]))
    if maganhangzok_szama(napok[i]) > maganhangzok_szama(napok[maxi_mgh]):
        maxi_mgh = i
print(f'A legtöbb magánhangzó a {napok[maxi_mgh]}-ben van!')
