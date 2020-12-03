# Kérje be és tárolja el egy háromszög oldalait valós|egész típusú változókba,
# majd határozza meg és írja ki, hogy a háromszög megszerkeszthető-e!
# (A háromszög akkor megszerkeszthető, ha bármely két oldalának
# az összege nagyobb mint a harmadik oldal.)

# Lehetséges megoldás:

print('Háromszög szerkeszthetősége')
print('Kérem a háromszög oldalait!')
a: float = float(input('a = '))
b: float = float(input('b = '))
c: float = float(input('c = '))

if a+b > c and b+c > a and a+c > b:
    print('A háromszög megszerkeszthető!')
else:
    print('A háromszög nem szerkeszthető a megadott adatokkal!')
