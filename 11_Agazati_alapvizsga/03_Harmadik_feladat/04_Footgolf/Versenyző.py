from typing import List


class Versenyző:
    név: str
    ketegória: str
    egyesület: str
    pontszámok: List[int]

    def __init__(self, sor: str) -> None:
        m: List[str] = sor.split(';')
        self.név = m[0]
        self.ketegória = m[1]
        self.egyesület = m[2]
        self.pontszámok = []
        for i in range(3, len(m)):
            aktPont: int = int(m[i])
            self.pontszámok.append(aktPont)

    # 4. Készítsen függvényt vagy jellemzőt, amivel meghatározza egy versenyzőnek a
    # bajnokságban (8 fordulóban) elért egyéni összpontszámát! Az összpontszám számítását a
    # következő szabályok alapján végezze:
    # • A versenyző legrosszabb két eredménye kiesik az összpontszámból. A maradék
    #   hat pontszámot össze kell adni.
    # • Ha a versenyző legrosszabb egy vagy két eredménye nem nulla, akkor a
    #   versenyzőnek az összpontszámába bele kell számítani azt a 10 pont bónuszt,
    # amelyet ezekben a fordulókban megkapott. Például:
    # „50;50;20;50;30;50;50;50” pontok esetén a „20” és a „30” pont kiesik, de
    # mivel a kieső pontszámok nem nullák, ezért az indulásért járó 10-10 pont bónuszt
    # megkapja, így összpontszáma: 6 × 50 + 10 +10 = 320.

    def összpont(self) -> int:
        # Az eredeti listából másolatot készítünk, hogy az eredeti sorrend ne vesszen el:
        pontszámok_rendezve: List[int] = list(self.pontszámok)
        pontszámok_rendezve.sort()  # Lista rendezése
        összeg: int = 0
        for pont in pontszámok_rendezve[2:]:
            összeg += pont
        if pontszámok_rendezve[0] != 0:
            összeg += 10
        if pontszámok_rendezve[1] != 0:
            összeg += 10
        return összeg
