print('Osztályok - objektumok')
# Az osztály a programozási nyelvek legfontosabb összetett adattípusai
# Biztosítják az adatok és a rajtuk műveletet végző függvények (kódtagok) egységét
# A függvényeket gyakran metódusoknak hívjuk
# Az osztály változóit (adattagjait) gyakran mezőknek is hívjuk
# Az adat- és kódtagok klasszikus láthatósági szintjét (public, private, protected, stb.)
#   a Python nem különbözteti meg, a protected tagok jelölésére van csak módunk (de ezt nem tesszük meg)
# Egy osztályt leggyakrabban csak példányosítás után használhatunk
# Az osztály konstruktora egy speciális metódus, jellemzően az adattagok inicializálását végzi,
#   felkészíti az osztálypéldányt a használatra
# A konstruktor automatikusan hívódik az osztálypéldány létrehozásakor
# A konstruktor Pythonban kötelezően az __init__ nevet kapja
# Az osztálypéldányt gyakran objektumnak is hívjuk
# A self foglalt szóval az aktuális osztálypéldány adat- és kódtagjait érjük el osztályon belül,
#   kötelezően minden kódtag első paramétere, adattípus nélkül
# A Python forrásállomány neve gyakran az osztály nevével egyezik meg (itt homerseklet.py kéne hogy legyen)
# Ha az osztályra másik forrásállományba van szükségünk, akkor azt importálni kell, pl.:
#   from homerseklet import Homerseklet

# A Homerseklet osztály definiálása:


class Homerseklet:  # a class foglalt szó után adjuk meg az osztály azonosítóját (nevét)
    ertekfok: float  # adattag (mező)
    feldolgozas_alatt: bool  # adattag (mező)

    def __init__(self, ertek_fok: float) -> None:  # az osztály konstruktora, speciális metódusa
        self.ertekfok = ertek_fok
        self.feldolgozas_alatt = False

    def valtoztat(self, delta_fok: float) -> None:  # az osztály kódtagja, metódusa
        self.ertekfok += delta_fok

    def ertekfahrenheit(self) -> float:  # az osztály kódtagja, metódusa
        return (self.ertekfok * 1.8) + 32


testho: Homerseklet = Homerseklet(37)  # osztálypéldány (objektum) létrehozása
# testho => objektum (osztálypéldány) azonosítója (neve)
# Homerseklet => Osztály azonosítója (neve)
# Homerseklet(37) => Osztály konstruktora az aktuális (37) paraméterrel
# A példány (objektum) létrehozásakor a konstruktor (__init__) automatikusan meghívásra kerül

# az adattagok osztálypéldány felől is elérhetők (írhatók, olvashatók)
testho.feldolgozas_alatt = True
print(testho.feldolgozas_alatt)  # a tagok osztálypéldány felől is elérhetők (írhatók, olvashatók)
print(testho.ertekfok)
print(testho.ertekfahrenheit())
testho.ertekfok = 36.4

# kódtagok hívása:
print(testho.ertekfok)
testho.valtoztat(10.5)
print(testho.ertekfok)
