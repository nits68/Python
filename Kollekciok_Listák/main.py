def main():
    #  Lista létrehozása:
    lista1 = ['barack', 'körte', 'szilva', 'alma', 'szőlő']  # Elemekkel inicializált lista
    lista2 = []   # Üres lista
    lista3 = list()  # list() konstruktorral létrehozott üres lista
    lista4 = list({'a', 'e', 'i', 'o', 'u'})  # list() konstruktorral halmazból létrehozott lista

    # Teljes lista kiírása
    print(lista1)  # ['barack', 'körte', 'szilva', 'alma', 'szőlő']

    # Hivatkozás lista elemeire (indexelés)
    # Listák elemit 0-tól indulva egész számokkal indexeljük:
    print(lista1[0])  # barack
    # indexelés index tartománnyal
    print(lista1[1:3])  # ['körte', 'szilva']
    print(lista1[1:])  # ['körte', 'szilva', 'alma', 'szőlő']
    print(lista1[:2])  # ['barack', 'körte']
    # negatív indexet is használhatunk:
    print(lista1[-1])  # szőlő
    print(lista1[-3:-1])  # ['szilva', 'alma']

    # Értékadás
    lista1[0] = 'alma'
    print(lista1)
    lista1[0] = True  # A lista elemi bármikor válthatják típusukat
    lista1[1] = 123
    print(lista1)

    # Lista bejárása index nélkül
    for i in lista1:
        print(f'{i} ', end='')  # True 123 szilva alma szőlő
    print()  # Soremelés
    # Lista bejárása indexekkel
    for index, item in enumerate(lista1):
        print(f'lista1[{index}]={item} ', end='')  # True 123 szilva alma szőlő
    print()  # Soremelés

    # Tartalmazás vizsgálat az IN oprátorral
    if 'alma' in lista1:
        print('Az alma érték megtalálható a listában!')

    # Lista eleminek száma, lista "hossza": len() függvény
    print(F'A lista1 lista elemeinek száma: {len(lista1)}')  # 5








if __name__ == '__main__':
    main()
