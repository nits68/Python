# szekvencia = utasítások végrehajtása fentről-lefelé (top-down)
# Az utasítások végrehajtásának sorrendjét a "leírás sorrendje" határozza meg

# Csak szekvenciát tartalmazó egyszerű program
# (Téglalap kerület-terület meghatározás)

print('Téglalap kerülete és területe')
print('Adja meg a téglalap oldalait!')
oldal_a = float(input('a= '))
# szöveges típusú adat bekérése: input('a= ')
# szöveges típusú adat konvertálása valós számra: float("3.14")
# programban használt operátorok:
# "+" - összeadás
# "*" - szorzás
# "=" - értékadás
# "(", ")" - zárójelek (függvények paraméterei, műveleti sorrend felülbírálása)

oldal_b = float(input('b= '))
terulet = oldal_a * oldal_b
kerulet = 2 * (oldal_a + oldal_b)

# f-string: olyan speciális string literál, melybe változók, kifejezések értékei integrálhatók
# pl.: f'K = {kerulet}', vagy: f'T = {oldal_a * oldal_b}'
print(f'T = {terulet}')
print(f'K = {kerulet}')
