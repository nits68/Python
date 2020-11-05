print('Szám faktoriálisa')
n = int(input('n = '))
faktor = 1
for i in range(2, n + 1):  # i = 2, 3, 4, 5
    faktor = faktor * i  # 1 * 2, 2 * 3, 6 * 4, 24 * 5
print(f'n != {faktor}')
print(type(faktor))

print('Számok faktoriálisa 10-30 között')
for n in range(10, 31):
    faktor = 1
    for i in range(2, n + 1):  # i = 2, 3, 4, 5
        faktor = faktor * i  # 1 * 2, 2 * 3, 6 * 4, 24 * 5
    print(f'n != {faktor}')
