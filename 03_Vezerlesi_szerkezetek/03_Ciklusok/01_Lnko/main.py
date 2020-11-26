print('LNKO kivonásos algoritmussal')
a: int = int(input('a = '))
b: int = int(input('b = '))
while a != b:
    if a > b:
        a = a - b
    else:
        b = b - a
print(f'LNKO = {a}')

print('LNKO Euklideszi algoritmussal')
a: int = int(input('a = '))
b: int = int(input('b = '))
m: int = -1  # biztosan lesz egy CM végrehajtás
#  így helyettesíthető a klasszikus hátultesztelő ciklus Python-ban
while m != 0:
    m = a % b  # osztás maradéka
    a = b  # 2. ismétléstől az előző maradék kerül "a" változóba
    b = m  # Eukleidész: Az utolsó nem nulla maradék a LNKO
print(f'LNKO = {a}')
