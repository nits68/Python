class Épület:
    név: str
    ország: str
    város: str
    magasság: float
    emelet: int
    épült: int

    def __init__(self, sor: str) -> None:
        név, város, ország, magasság, emelet, épült = sor.split(';')
        self.név = név
        self.ország = ország
        self.város = város
        self.magasság = float(magasság.replace(',', '.'))
        self.emelet = int(emelet)
        self.épült = int(épült)
