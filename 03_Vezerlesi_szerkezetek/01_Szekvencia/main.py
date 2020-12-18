def main() -> None:
    # szekvencia vezérlési szerkezet: utasítások végrehajtása fentről-lefelé (top-down)
    # Az utasítások végrehajtásának sorrendjét a "leírás sorrendje" határozza meg

    # Csak szekvenciát tartalmazó egyszerű program: Téglalap kerület-terület meghatározás

    # print() függvény: változók, literálok és kifejezések értkének megjelenítése a console ablakban
    print('Téglalap kerülete és területe')
    print('Adja meg a téglalap oldalait!')
    a: float = float(input('a= '))
    # szöveges típusú adat bekérése: input('a= ')
    # szöveges típusú adat konvertálása valós számra: float('3.14')
    # programban használt operátorok:
    # "+" - összeadás
    # "*" - szorzás
    # "=" - értékadás
    # "(", ")" - zárójelek (függvények paraméterei, műveleti sorrend felülbírálása)

    b: float = float(input('b= '))
    terület: float = a * b
    kerület: float = 2 * (a + b)

    # f-string: olyan speciális string literál, melybe változók, kifejezések értékei integrálhatók
    # pl.: f'K = {kerulet}', vagy: f'T = {oldal_a * oldal_b}'
    print(f'T = {terület}')
    print(f'K = {kerület}')


if __name__ == "__main__":
    main()
