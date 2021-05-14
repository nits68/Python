# from typing import List # Python 3.8.X, vagy alatta kell


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
        # m: List[str] = sor.split(';') # Python 3.8.X, vagy alatta
        # m: list[str] = sor.split(';')
        # self.ora = int(m[0])
        # self.perc = int(m[1])
        # self.adas_db = int(m[2])
        # self.nev = m[3]

    def atszamol_percre(self) -> int:
        return self.ora * 60 + self.perc
