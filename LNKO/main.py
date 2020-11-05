import sys

print('LNKO kivonásos algoritmussal')
a = int(input('a = '))
b = int(input('b = '))
while a != b:
    if a > b:
        a = a - b
    else:
        b = b - a
print(f'LNKO = {a}')

print('LNKO Euklideszi algoritmussal')
a = int(input('a = '))
b = int(input('b = '))
m = -1  # biztosan lesz egy CM végrehajtás
#  így helyettesíthető a klasszikus hátultesztelő ciklus Python-ban
while m != 0:
    m = a % b  # osztás maradéka
    a = b  # 2. ismétléstől az előző maradék kerül "a" változóba
    b = m  # Euklidesz: Az utolsó nem nulla maradék a LNKO
print(f'LNKO = {a}')
