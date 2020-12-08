class Eredmény:
    # Versenyzo;Rajtszam;Kategoria;Versenyido;TavSzazalek
    név: str
    rajtszám: int
    ketegória: str
    idő: str
    táv_százalék: int

    def __init__(self, sor: str) -> None:
        név, rajtszám, kategória, idő, táv_százalék = sor.split(';')
        self.név = név
        self.rajtszám = int(rajtszám)
        self.ketegória = kategória
        self.idő = idő
        self.táv_százalék = int(táv_százalék)

    def név_hossz(self) -> int:
        return len(self.név)

    def idő_óra(self) -> float:
        óra, perc, mp = self.idő.split(':')
        return int(óra) + int(perc) / 60 + int(mp) / 3600
