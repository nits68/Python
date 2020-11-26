# Szelekciók (elágazások)
# Olyan vezérlési szerkezetek, ahol feltételekhez köthetjük az utasítások végrehajtását

# Elágazások fajtái:
# - egy ágú (if)
# - kétágú (if-else)
# - többágú (if-elif-elif- ... -elif-else) (switch-case szerkezet nincs a Python-ban)

# Példa egyágú (if) szelekcióra:
print('Szám abszolút értéke')
inputX: int = int(input('x= '))
absX: int = inputX
if inputX < 0:
    absX = inputX * -1
print(f'Abs({inputX}) = {absX}')

# Példa kétágú (if-else) elágazásra
print('\nPáros-páratlan meghatározása')
inputSzam: int = int(input('szam= '))
if inputSzam % 2 == 0:
    print('A szám páros!')
else:
    print('A szám páratlan!')

# Példa többágú (if-elif-else) elágazásra (else "ág" elhagyható):
print('\nOsztályzat szöveges megfelelője')
erdemjegy: int = int(input('Kérem az osztályzatot [1-5]: '))
if erdemjegy == 1:
    print('Elégtelen')
elif erdemjegy == 2:
    print('Elégséges')
elif erdemjegy == 3:
    print('Közepes')
elif erdemjegy == 4:
    print('Jó')
elif erdemjegy == 5:
    print('Jeles')
else:
    print('Ez nem osztályzat!')


# Rövidített (shorthand) kétágú elágazás, amit feltételes operátor funkcióját is betöltheti:
a: int = 10
b: int = 20
print("A") if a > b else print("B")
c: int = 12 if a != b else 24
# A fenti értékadás C# feltételes operátorral:
# c = a != b ? 12 : 24
print(c)  # 12

# A pass utasítást akkor használjuk, ha később szeretnék egy igaz-hamis ág (blokk) utastásait megadni,
# de kerülni szeretnénk a szintaktikai hibákat
if b > a:
    pass
else:
    pass
