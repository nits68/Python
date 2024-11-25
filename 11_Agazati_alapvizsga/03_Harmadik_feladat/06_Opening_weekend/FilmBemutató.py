class FilmBemutató(object):
    eredeti_cím: str
    magyar_cím: str
    bemutató: str
    fogalmazó: str
    bevétel: int
    látogató: int

    def __init__(self, sor: str) -> None:
        m: list[str] = sor.split(";")
        self.eredeti_cím = m[0]
        self.magyar_cím = m[1]
        self.bemutató = m[2]
        self.fogalmazó = m[3]
        self.bevétel = int(m[4])
        self.látogató = int(m[5])
