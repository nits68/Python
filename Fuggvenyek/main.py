# Függvény fogalma: Jól meghatározott feladatot ellátó utasítások csoportja

# A függvényt használat előtt definiálni kell
# A függvény definíció általános alakja (szintaxisa):
# 1. Függvény fej leírása:
#    =====================
#    def függvény_azonosítója(formális paraméterlista) -> függvény_visszatérési_értékének_a_típusa:
# 2: Függvény törzs leírása:
#    ======================
#    tetszőleg számú utasítás, legalább egy return utasítás (gyakran az utolsó utasítás)
#
# Minta:
def osszead(a: int, b: int) -> int:  # függvény feje, a,b: formális paraméterek
    return a + b  # függvény törzse


def lnko(a: int, b: int) -> int:
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a


print('Alprogramok - függvények')
# A függvény használata, hívása:
# A hívás szintaxisa:
# függvény_azonosítója(aktuális paraméterlista)
osszead(3, 4)  # A függvény visszatérési értéke így elveszik
print(osszead(3, 4))
print('Két szám legnagyobb közös osztója')
a: int = int(input('a = '))
b: int = int(input('b = '))
print(f'LNKO({a}, {b}) = {lnko(a, b)}')
