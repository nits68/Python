# Szelekciók (elágazások)
# Olyan vezérlési szerkezetek, ahol feltételekhez köthetjük az utasítások végrehajtását
# Elágazások fajtái:
# - egy ágú (if)
# - kétágú (if-else)
# - többágú (if-elif-elif- ... -elif-else) (switch-case szerkezet nincs a Python-ban)

# Példa egyágú (if) szelekcióra:
print('Szám abszolút értéke')
inputX = int(input('x= '))
absX = inputX
if inputX < 0:
    absX = inputX * -1
print(f'Abs({inputX}) = {absX}')

# Példa kétágú (if-else) elágazásra
print('\nPáros-páratlan meghatározása')
inputSzam = int(input('szam= '))
if inputSzam % 2 == 0:
    print('A szám páros!')
else:
    print('A szám páratlan!')

# Példa többágú (if-elif-else) elágazásra:
print('\nOsztályzat szöveges megfelelője')
erdemjegy = int(input('Kérem az osztályzatot [1-5]: '))
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
