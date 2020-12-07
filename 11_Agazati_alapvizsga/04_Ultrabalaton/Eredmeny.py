class Eredmeny:
    # Versenyzo;Rajtszam;Kategoria;Versenyido;TavSzazalek
    Nev: str
    Rajtszam: int
    Kategoria: str
    Veresenyido: str
    TavSzazalek: int

    def __init__(self, sor: str) -> None:
        Nev, Rajtszam, Kategoria, Versenyido, TavSzazalek = sor.split(';')
        self.Nev = Nev
        self.Rajtszam = int(Rajtszam)
        self.Kategoria = Kategoria
        self.Veresenyido = Versenyido
        self.TavSzazalek = int(TavSzazalek)

    def nev_hossz(self) -> int:
        return len(self.Nev)

    def verseny_ido_ora(self) -> float:
        ora, perc, mp = self.Veresenyido.split(':')
        return int(ora) + int(perc) / 60 + int(mp) / 3600
