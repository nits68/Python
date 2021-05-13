def main() -> None:
    # Iteráció (ciklus): Olyan vezérlési szerkezet, melyet utasítás(ok) ismétlésére használunk
    # Ciklusok fajtái:
    # - klasszikus növekményes ciklus (for, NINCS a Python-ban)
    # - for-in ciklus (speciális ciklus a Python-ban, C# foreach ciklushoz hasonlít leginkább)
    # - elöltesztelő ciklus (while)
    # - hátultesztelő ciklus (NINCS a Python-ban)

    # w3s: https://www.w3schools.com/python/python_for_loops.asp

    # Klasszikus növekményes ciklus megvalósítása for-in ciklussal:
    for i in range(8):  # range osztály számsorozatot állít elő (0, 1, 2, 3, ..., 6, 7)
        print(i, end=' ')  # 0 1 2 3 4 5 6 7
    print()

    for i in range(-5, 5):
        print(i, end=' ')  # -5 -4 -3 -2 -1 0 1 2 3 4
    print()

    for i in range(1, 11, 2):
        print(i, end=' ')  # 1 3 5 7 9
    print()

    # lista, összetett adatszerkezet, több adatot tárol
    t: list[str] = ['alma', 'körte', 'szilva']
    # t[0] -> 'alma'
    # t[1] -> 'körte'
    # t[2] -> 'sziva'
    for i in range(len(t)):
        print(f't[{i}]={t[i]}', end=' ')  # t[0]=alma t[1]=körte t[2]=szilva
    print()

    # for e in t:
    #     print(e)

    # A break utasítás: segítségével kiléphetünk a ciklusból,
    # befejezzük az ismétlést a ciklusfeltétel tesztelése nélkül.
    print('A break utasítás')
    i: int = 1
    while i < 6:
        print(i, end=' ')  # 1 2 3
        if i == 3:
            break
        i += 1
    print()

    # Elöltesztelő ciklus (while):
    # w3c: https://www.w3schools.com/python/python_while_loops.asp

    # A continue utasítás: segítségével befejezzük a ciklusmag aktuális végrehajtását,
    # a ciklusfeltétel (i < 6) tesztelésével folytatjuk a kódot
    print('A continue utasítás')
    i: int = 0
    while i < 6:
        i += 1
        if i == 3:
            continue
        print(i, end=' ')  # 1 2 4 5 6
    print()

    i: int = 1
    while i < 10:
        i += 1
        if i % 2 == 1:
            continue
        print(i, end=' ')  # 2 4 6 8 10
    print()


if __name__ == "__main__":
    main()

# Program nyomkövetése, változók vizsgálata
# 1. töréspont (breakpoint) elhelyezése
# 2. Nyomkövetés indítása F5
# 3. Az első töréspontnál megáll a program futása
# 4. Lehetőségünk van a változók értékeinek vizsgálatára
# és a utasítások végrahjtását (az algoritmust) vizsgálhatjuk
# az F10 (step over) és F11 (step into) billentyűkkel
# 5. Ha végeztünk, akkor két lehetőség van:
#    - program folytatása: F5
#    - program (nyomkövetés) leállítása: Shift-F5
