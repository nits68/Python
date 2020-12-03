# import math

# 1. Kérjen be két (egész|valós) számot, majd
#    írja ki, hogy melyik a nagyobb és melyik a kisebb szám!

# 2. Kérje be egy háromszög oldalait, majd határozza meg,
#    hogy a háromszög megszerkeszthető-e!
#    (A háromszög akkor megszerkeszthető, ha bármely két oldalának
#     az összege nagyobb mint a harmadik oldal)

# 3. Kérje be egy háromszög oldalait, majd határozza meg,
#    a háromszög területét és kerületét a Heron képlet segítségével!
#    Feltételezheti, hogy az input adatokból háromszög szerkeszthető!
#    Heron képlet: s = K/2
#    T = Gyök(s*(s-a)*(s-b)*(s-c))

# Megoldás:
# print('Háromszög kerülete és területe')
# print('Kérem az oldalakat')
# a: float = float(input('a = '))
# b: float = float(input('b = '))
# c: float = float(input('c = '))
# kerulet: float = a+b+c
# s: float = kerulet / 2
# terulet: float = math.sqrt(s*(s-a)*(s-b)*(s-c))
# print(f'K = {kerulet}')
# print(f'T = {terulet}')

# 4. Kérje be egy téglalap oldalait, majd határozza meg,
#    a téglalap területét és kerületét!
#    A területet és a kerületet a következő képletekkel számolja:
#    T = a * b
#    K = 2 *(a + b)

# 5. Határozza meg két egész szám legnagyobb közös osztóját a következő
#    algoritmussal: Mindaddig kisebbítse a nagyobb számot a kisebb számmal,
#    amíg a két szám egyenlő nem lesz! Az így kapott szám lesz a
#    legnagyobb közös osztó.
