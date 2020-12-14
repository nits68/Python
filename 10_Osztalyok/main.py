# Az osztály a programozási nyelvek legfontosabb összetett adattípusai
# Biztosítják az adatok és a rajtuk műveletet végző függvények (kódtagok) egységét
# A függvényeket gyakran metódusoknak hívjuk
# Az osztály változóit (adattagjait) gyakran mezőknek is hívjuk
# Az adat- és kódtagok klasszikus láthatósági szintjét (public, private, protected, stb.)
#   a Python nem különbözteti meg, a protected tagok jelölésére van csak módunk (de ezt nem tesszük meg az alapozó vizsgáig)
# Egy osztályt leggyakrabban csak példányosítás után használhatunk
# Az osztály konstruktora egy speciális metódus, jellemzően az adattagok inicializálását végzi,
#   felkészíti az osztálypéldányt a használatra
# A konstruktor automatikusan hívódik az osztálypéldány létrehozásakor
# A konstruktor Pythonban kötelezően az __init__ nevet kapja
# Az osztálypéldányt gyakran objektumnak is hívjuk
# A self foglalt szóval az aktuális osztálypéldány adat- és kódtagjait érjük el osztályon belül,
#   kötelezően minden kódtag első paramétere, adattípus nélkül
# A Python forrásállomány neve gyakran az osztály nevével egyezik meg (itt Hőmérséklet.py kéne hogy legyen)
# Ha az osztályra másik forrásállományba van szükségünk, akkor azt importálni kell, pl.:
#   from Hőmérséklet import Hőmérséklet

# A Homerseklet osztály definiálása:

class Hőmérséklet:  # a class foglalt szó után adjuk meg az osztály azonosítóját (nevét)
    érték_fok: float  # adattag (mező)
    feldolgozás_alatt: bool  # adattag (mező)

    def __init__(self, értek_fok: float) -> None:  # az osztály konstruktora, speciális metódusa
        self.érték_fok = értek_fok
        self.feldolgozás_alatt = False
        # A konstruktorban is létrehozhatunk adattagokat, de ezt javasolt elkerülni!

    def valtoztat(self, delta_fok: float) -> None:  # az osztály kódtagja, metódusa
        self.érték_fok += delta_fok

    def értek_fahrenheit(self) -> float:  # az osztály kódtagja, metódusa
        return (self.érték_fok * 1.8) + 32


def main() -> None:
    print('Osztályok - objektumok')
    testhő: Hőmérséklet = Hőmérséklet(37)  # osztálypéldány (objektum) létrehozása
    # testho => objektum (osztálypéldány) azonosítója (neve)
    # Homerseklet => Osztály azonosítója (neve)
    # Homerseklet(37) => Osztály konstruktora az aktuális (37) paraméterrel
    # A példány (objektum) létrehozásakor a konstruktor (__init__) automatikusan meghívásra kerül

    # az adattagok elérése osztálypéldány felől
    testhő.feldolgozás_alatt = True
    print(testhő.feldolgozás_alatt)  # a tagok osztálypéldány felől is elérhetők (írhatók, olvashatók)
    print(testhő.érték_fok)
    testhő.érték_fok = 36.4
    print(testhő.érték_fok)

    # kódtagok hívása:
    print(testhő.értek_fahrenheit())
    testhő.valtoztat(10.5)

    print(testhő.érték_fok)


if __name__ == "__main__":
    main()
