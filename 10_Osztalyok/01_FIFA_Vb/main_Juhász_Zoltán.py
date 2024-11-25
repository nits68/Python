class Csapat:
    def __init__(self, sor: list[str]):
        self.orszag: str = sor[0]
        self.reszvetelekSzama: int = int(sor[1])
        self.elsoIndulas: int = int(sor[2])
        self.legutobbiIndulas: int = int(sor[3])
        self.legjobbEredmeny = sor[4]
        self.elsoOtaElteltEv: int = 2021 - self.elsoIndulas


csapatok: list[Csapat] = []
# 0. feladat:
for sor in open('fociVBk.csv', encoding='UTF-8').read().splitlines()[1:]:
    csapatok.append(Csapat(sor.split(';')))
# 1. feladat:
print(f'1. feladat: csapatok száma: {len(csapatok)}')

# 2. feladat:
print('\n2. feladat: 2018as VB csapatai:')
i = 1
for cs in csapatok:
    if cs.legutobbiIndulas == 2018:
        print('%15s' % cs.orszag, end='')
        if i % 4 == 0:
            print('')
        i += 1

# 3. feladat:
sum = 0
for cs in csapatok:
    if cs.orszag in ['Belgium', 'Hollandia', 'Luxemburg']:
        sum += cs.reszvetelekSzama
print(f'\n3. feladat: A BeNeLux országok összesen {sum} alkalommal vettek részt a VBn')

# 4. feladat:
mini = 0
i = 0
for i in range(1, len(csapatok)):
    if csapatok[i].elsoIndulas < csapatok[mini].elsoIndulas:
        mini = i
elso = csapatok[mini].elsoIndulas
print(f'\n4. feladat: Az első VBt {elso}-ban rendezték')

# 5. feladat:
c = 0
for cs in csapatok:
    if('Világbajnok' in cs.legjobbEredmeny):
        c += 1
print(f'\n5. feladat: Eddig {c} ország csapata volt világbajnok')

# 6. feladat:
print('\n6. feladat:', end=' ')
i = 0
while i < len(csapatok):
    if csapatok[i].orszag == 'Szlovákia':
        print(f'Szlovákia legjobb eredménye: {csapatok[i].legjobbEredmeny}')
        break
    i += 1
else:
    print(f'Szlovákia még sosem került ki a VBre')

# 7. feladat:
print('\n7. feladat:', end=' ')
i = 0
while i < len(csapatok):
    if csapatok[i].orszag == 'Magyarország':
        if csapatok[1].elsoIndulas == elso:
            print('Magyarország kijutott az első VBre')
        else:
            print('Magyarország nem jutott ki az első VBre')
        break
    i += 1
else:
    print('Magyarország sosem jutott ki VB-re')

# 8: feladat:
file = open('legtobbszor.txt', 'w', encoding='UTF-8')
for cs in csapatok:
    if(cs.reszvetelekSzama >= 10):
        file.write(f'{cs.orszag} {cs.elsoOtaElteltEv}\n')
file.close()
print('\n8. feladat: legtobbszor.txt kész!')
