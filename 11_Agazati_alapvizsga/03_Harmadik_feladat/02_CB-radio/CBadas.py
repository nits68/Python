# from typing import List


class CBadas:
    ora: int
    perc: int
    adas_db: int
    nev: str

    def __init__(self, sor: str) -> None:
        ora, perc, adas_db, nev = sor.split(';')
        self.ora = int(ora)
        self.perc = int(perc)
        self.adas_db = int(adas_db)
        self.nev = nev
        # vagy:
        # m: List[str] = sor.split(';')
        # self.ora = int(m[0])
        # self.perc = int(m[1])
        # self.adas_db = int(m[2])
        # self.nev = m[3]

    def atszamol_percre(self) -> int:
        return self.ora * 60 + self.perc
