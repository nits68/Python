print('Osztályok - objektumok')
# Az osztály a programozási nyelvek legfontosabb összetett adattípusai
# Biztosítják az adatok és a rajtuk műveletet végző függvények (kódtagok) egységét
# A függvényeket gyakran metódusoknak hívjuk
# Az osztály változóit (adattagjait) gyakran mezőknek is hívjuk
# Az adat- és kódtagok láthatósági szintjét (public, private, protected, stb.)
#   a Python nem különbözteti meg, a protected tagok jelölésére van csak módunk
# Egy osztályt leggyakrabban csak példányosítás után használhatunk
# Az osztály konstruktora egy speciális metódus, jellemzően az adattagok inicializálását végzi,
#   felkészíti az osztálypéldányt a használatra
# A konstruktor automatikusan hívódik az osztálypéldány létrehozásakor
# A konstruktor Pythonban kötelezően az __init__ nevet kapja
# Az osztálypéldányt gyakran objektumnak is hívjuk
# A jellemzők speciális kódtagok, gyakran egy protected mező írását és olvasását felügyelik
# A self foglalt szóval az aktuális osztálypéldány adat- és kódtagjait érjük el,
#   kötelezően minden kódtag első paramétere

# A Homerseklet osztály definiálása:


class Homerseklet:  # a class foglalt szó után adjuk meg az osztály azonosítóját (nevét)
    _ertekfok: float  # adattag (mező) protected jelzéssel (_), csak az osztály kódtagjai érhetik el, használhatják
    feldolgozas_alatt: bool  # publikus mező, kódtagokból és osztálypéldány felől is elérhető

    def __init__(self, ertek_fok: float = 0) -> None:  # az osztály konstruktora, speciális metódusa
        self.ertekfok = ertek_fok
        self.feldolgozas_alatt = False

    def valtoztat(self, delta_fok: float) -> None:  # az osztály publikus kódtagja, metódusa
        self.ertekfok += delta_fok

    @property
    def ertekfahrenheit(self) -> float:  # csak olvasható jellemző (nincs setter)
        return (self._ertekfok * 1.8) + 32

    @property
    def ertekfok(self) -> float:  # írható / olvasható jellemző (van setter)
        return self._ertekfok

    @ertekfok.setter
    def ertekfok(self, ertek_fok: float) -> None:
        if ertek_fok < -273.15:
            raise ValueError('-273 foknál kisebb nem lehetséges')
        self._ertekfok = ertek_fok


testho: Homerseklet = Homerseklet(37)  # osztálypéldány (objektum) létrehozása

print(testho.feldolgozas_alatt)  # a publikus tagok osztálypéldány felől is elérhetőek
# print(testho._ertekfok)  # Pylance figyelmeztetés:
# "_ertekfok" is protected and used outside of the class in which it is declaredPylance (reportPrivateUsage)

print(testho.ertekfok)  # jellemző olvasása
testho.ertekfok = 36.4  # jellemző írása
print(testho.ertekfahrenheit)  # jellemző olvasása
# testho.ertekfahrenheit = 100  # jellemző írása - Pylance figyelmeztetés:
# Cannot assign member "ertekfahrenheit" for type "Homerseklet"  Property "ertekfahrenheit" has no defined setterPylance

try:
    proba: Homerseklet = Homerseklet(-300)  # osztálypéldány (objektum) létrehozása
except Exception as ex:
    print(f'Hiba __doc__: {ex.__doc__}')
    print(f'Hibaüzenet: {ex.args[0]}')

try:
    while True:
        testho.valtoztat(-50)  # osztály metódusának hívása (paramétere csak metódusnak lehet)
        print(testho.ertekfok)
except Exception as ex:
    print(f'Hiba __doc__: {ex.__doc__}')
    print(f'Hibaüzenet: {ex.args[0]}')
