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
#  így helyettesíthető a klasszikus hátultesztelő ciklus
while m != 0:
    m = a % b  # osztás maradéka
    a = b  # 2. ismétléstől az előző maradék kerül "a" változóba
    b = m  # Euklidesz: Az utolsó nem nulla maradék az LNKO
print(f'LNKO = {a}')

print('Szám faktoriálisa')
n = int(input('n = '))
faktor = 1
for i in range(2, n + 1):  # i = 2, 3, 4, 5
    faktor = faktor * i  # 1 * 2, 2 * 3, 6 * 4, 24 * 5
print(f'n != {faktor}')
print(type(faktor))

print('Számok faktoriálisa 50-100 között')
for n in range(50, 101):
    faktor = 1
    for i in range(2, n + 1):  # i = 2, 3, 4, 5
        faktor = faktor * i  # 1 * 2, 2 * 3, 6 * 4, 24 * 5
    print(f'n != {faktor} {faktor.bit_length()}')

#  lista bejárása
napok = ['hétfő', 'kedd', 'szerda', 'csütörtök', 'péntek']
for i in napok:
    print(i, end=' ')  # kiírást lezáró karakter, alapért.: \n
print()  # soremelés a konzol ablakban

#  lista bejárása fordítva
napok.reverse()
for i in napok:
    print(i, end=' ')
print()
