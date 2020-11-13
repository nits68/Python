# program = algoritmus + adatszerkezet
# algoritmus -> utasítások végrehajtásának sorrendje,
#               amit vezérlési szerkezetek határoznak meg a prog. nyelvekben
# adatszerkezet -> programunkban használt változók halmaza

# Szekvencia vezérlési szerkezet
# (utasítások végrehajtása egymás után, top-down)
# táéjokoztatás > adatbekérés > számítás > eredmények közlése

# Változók: Adatok tárolására használt egységek
# Jellemzőik:
# - azonosító (InputTime C#, input_time Python)
# - típus (str, int, float, bool, stb.)
# - kezdőérték
# - aktuális érték

# Csak szekvenciát tartalmazó program
# (Téglalap kerület-terület meghatározás)

# Literál: Olyan adat, amihez nem rendelünk azonosítót
# sting literál: 'alma' vagy "alma"
# egész (int) literál: 345
# logikai (bool) literálok: True, False
# valós (float) literál: 5.6

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

# template string: olyan string literál,
# melybe változók, kifejezések értékei integrálhatók
# pl.: f'K = {kerulet}', vagy: f'T = {oldal_a * oldal_b}'
print(f'T = {terulet}')
print(f'K = {kerulet}')