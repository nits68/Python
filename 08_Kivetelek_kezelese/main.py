print('Kivételkezelés')

# A program futásakor bizonyos utasítások esetében felléphetnek hibák, melyeket a megfelelő szerkezettel kézben tarthatunk
# Ilyen hibák például az állományok kezelése során fellépő problémák, nullával osztás hibája vagy listák helytelen indexelése.

# A try-except blokk:
# A try blokkban helyezzük el a kritikus utasításokat, ahol hiba esetén az exception blokk kerül végrehajtásra
# Az exception blokk lehetővé teszi a hiba kezelését, jelzését.

try:
    szamlalo: int = int(input('Kérem a számlálót: '))
    nevezo: int = int(input('Kérem a nevezőt: '))
    tort: float = szamlalo / nevezo
    print(f'{szamlalo}/{nevezo} = {tort}')
except Exception as ex:  # Az Exception az osztályhierarchia tetején áll, minden hibaobjektumot "elkap"
    print(f'A hibaobjektum típusa: {type(ex)}')
    print(f'Hiba szövege: {ex}')
    print(f'Hiba dokumentációja : {ex.__doc__}')

# Ha a keletkezett hibaobjektum típusától függően más-más except blokkot kívánunk készíteni:
# Fontos: A használni kívánt hibaobjektumok felsorolása kötött, ha ős-leszármazott viszony áll fent
# Szabály: A hierarchia alján lévő leszármazottakkal kell kezdeni, majd jöhetnek az ősök
print('Több except blokk használata')
try:
    szamlalo: int = int(input('Kérem a számlálót: '))
    nevezo: int = int(input('Kérem a nevezőt: '))
    tort: float = szamlalo / nevezo
    print(f'{szamlalo}/{nevezo} = {tort}')
except ValueError as ex:  # Konverziós hibáknál ilyen típusú hibaobjektum keletkezik
    print('Konverziós hiba!')
    print(f'A hibaobjektum típusa: {type(ex)}')
    print(f'Hiba szövege: {ex}')
except ZeroDivisionError as ex:  # Ha nullával osztunk, akkor ilyen típusú hibaobjektum keletkezik
    print('Nullával osztani csak Chuck Norris tud!')
    print(f'A hibaobjektum típusa: {type(ex)}')
    print(f'Hiba szövege: {ex}')
except Exception as ex:  # Az Exception az osztályhierarchia tetején áll, minden más hibaobjektumot "elkap"
    print(f'A hibaobjektum típusa: {type(ex)}')
    print(f'Hiba szövege: {ex}')

print('Saját hibaobjektum készítése')


def Tort(szamlalo: float, nevezo: float) -> float:
    if nevezo == 0:
        raise ValueError('A nevező nem lehet nulla!')  # Saját hibaobjektum készítése
    return szamlalo / nevezo


try:
    szamlalo: int = int(input('Kérem a számlálót: '))
    nevezo: int = int(input('Kérem a nevezőt: '))
    print(f'{szamlalo}/{nevezo} = {Tort(szamlalo, nevezo)}')
except Exception as ex:  # Az Exception az osztályhierarchia tetején áll, minden más hibaobjektumot "elkap"
    print(f'A hibaobjektum típusa: {type(ex)}')
    print(f'Hiba szövege: {ex}')
    print(f'Hiba dokumentációja: {ex.__doc__}')


# A Python beépített hibaosztályai:
# ===============================
# BaseException
#  +-- SystemExit
#  +-- KeyboardInterrupt
#  +-- GeneratorExit
#  +-- Exception
#       +-- StopIteration
#       +-- StopAsyncIteration
#       +-- ArithmeticError
#       |    +-- FloatingPointError
#       |    +-- OverflowError
#       |    +-- ZeroDivisionError
#       +-- AssertionError
#       +-- AttributeError
#       +-- BufferError
#       +-- EOFError
#       +-- ImportError
#       |    +-- ModuleNotFoundError
#       +-- LookupError
#       |    +-- IndexError
#       |    +-- KeyError
#       +-- MemoryError
#       +-- NameError
#       |    +-- UnboundLocalError
#       +-- OSError
#       |    +-- BlockingIOError
#       |    +-- ChildProcessError
#       |    +-- ConnectionError
#       |    |    +-- BrokenPipeError
#       |    |    +-- ConnectionAbortedError
#       |    |    +-- ConnectionRefusedError
#       |    |    +-- ConnectionResetError
#       |    +-- FileExistsError
#       |    +-- FileNotFoundError
#       |    +-- InterruptedError
#       |    +-- IsADirectoryError
#       |    +-- NotADirectoryError
#       |    +-- PermissionError
#       |    +-- ProcessLookupError
#       |    +-- TimeoutError
#       +-- ReferenceError
#       +-- RuntimeError
#       |    +-- NotImplementedError
#       |    +-- RecursionError
#       +-- SyntaxError
#       |    +-- IndentationError
#       |         +-- TabError
#       +-- SystemError
#       +-- TypeError
#       +-- ValueError
#       |    +-- UnicodeError
#       |         +-- UnicodeDecodeError
#       |         +-- UnicodeEncodeError
#       |         +-- UnicodeTranslateError
#       +-- Warning
#            +-- DeprecationWarning
#            +-- PendingDeprecationWarning
#            +-- RuntimeWarning
#            +-- SyntaxWarning
#            +-- UserWarning
#            +-- FutureWarning
#            +-- ImportWarning
#            +-- UnicodeWarning
#            +-- BytesWarning
#            +-- ResourceWarning
