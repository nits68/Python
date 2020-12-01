class Fogadasi_fordulo():
    # osztály adattagjai (mezői):
    ev: int
    het: int
    forulo: int
    t13p1: int
    ny13p1: int
    eredmenyek: str

    # osztály kódtagjai (metódusai)
    # Osztály konstruktora (speciális metódus, felkészíti az osztálypéldányt a használatra)
    def __init__(self, sor: str) -> None:
        ev, het, fordulo, t13p1, ny13p1, eredmenyek = sor.split(';')
        self.ev = int(ev)
        self.het = int(het)
        self.forulo = int(fordulo)
        self.t13p1 = int(t13p1)
        self.ny13p1 = int(ny13p1)
        self.eredmenyek = eredmenyek

    def nem_volt_dontetlen(self) -> bool:  # osztály metódusa
        return self.eredmenyek.count('X') == 0
