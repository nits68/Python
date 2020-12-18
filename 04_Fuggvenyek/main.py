# Függvény fogalma: Azonosítóval ellátott, meghatározott feladatot ellátó utasítások csoportja

# A függvényt használat előtt definiálni kell
# A függvény definíció általános alakja (szintaxisa):
# 1. Függvény fej leírása:
#    =====================
#    def függvény_azonosítója(formális paraméterlista) -> függvény_visszatérési_értékének_a_típusa:
# 2: Függvény törzs leírása:
#    ======================
#    tetszőleg számú utasítás, legalább egy return utasítás (gyakran az utolsó utasítás)

# Példa:
def összead(a: int, b: int) -> int:  # függvény feje
    # def => függvény definíciót bevezető foglalt szó
    # összead => a függvény azonosítója (neve)
    # () => operátorok a paraméterek megadására
    # a: int, b: int => függvény formális paraméterei azonosítóval és típussal (típus opcionális)
    # -> => függvény visszatérési értékét ezután az "operátor" után adhatjuk meg (opcionális)
    # int => a függvény visszatérési értékének a típusa

    return a + b  # függvény törzse, a return foglalt szó után határozzuk meg a függvény visszatérési értékét


def lnko(a: int, b: int) -> int:
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a


def main() -> None:
    print('Alprogramok - függvények')
    # A függvény használata, hívása:
    # A hívás szintaxisa:
    # ===================
    # függvény_azonosítója(aktuális paraméterlista)
    összead(3, 4)  # A függvény visszatérési értéke így elveszik
    print(összead(3, 4))  # A függvény visszatérési értékét a képernyőre írjuk
    összeg: int = összead(3, 4)  # A függvény visszatérési értékét eltároljuk
    print(összeg)

    print('Két szám legnagyobb közös osztója')
    a: int = int(input('a = '))
    b: int = int(input('b = '))
    print(f'LNKO({a}, {b}) = {lnko(a, b)}')

    # A Python programozási nyelv fontosabb (Ágazati alapvizsgára ismerendő) beépített függvényei:

    # abs() Returns the absolute value of a number - Szám abszolút értéke
    # chr() Returns a character from the specified Unicode code. - "Karakter" Unikód-ja
    # dir()	Returns a list of the specified object's properties and methods - Objektum adat- és kódtagjai
    # enumerate() Takes a collection and returns it as an enumerate object - Kollekció enumerálása (i, e)
    # id() Returns the id of an object - Objektum azonosítója
    # input() Allowing user input - Felhasználói input
    # len() Returns the length of an object - Az objektum hossza (pl.: lista elemszáma)
    # max()	Returns the largest item in an iterable - Maximum érték meghatározása
    # min() Returns the smallest item in an iterable - Minimum érték meghatározása
    # open() Opens a file and returns a file object - File objektum megnyitása/létrehozása
    # ord()	Convert an integer representing the Unicode of the specified character - Unikód-hoz tartozó karakter
    # print() Prints to the standard output device - Képernyőre írás
    # range() Returns a sequence of numbers, starting from 0 and increments by 1 - Számsorozat előállítása
    # sum() Sums the items of an iterator - Összeg meghatározása
    # type() Returns the type of an object - Objektum adattípusa (osztálya)

    # Konstruktor függvények:

    # bool() Returns the boolean value of the specified object
    # dict() Returns a dictionary (Array)
    # float() Returns a floating point number
    # int() Returns an integer number
    # list() Returns a list
    # set()	Returns a new set object
    # str() Returns a string object
    # tuple() Returns a tuple

    # Egyéb beépített függvények:

    # all() Returns True if all items in an iterable object are true
    # any() Returns True if any item in an iterable object is true
    # ascii() Returns a readable version of an object. Replaces none-ascii characters with escape character
    # bin() Returns the binary version of a number
    # bytearray() Returns an array of bytes
    # bytes() Returns a bytes object
    # callable() Returns True if the specified object is callable, otherwise False
    # classmethod() Converts a method into a class method
    # compile() Returns the specified source as an object, ready to be executed
    # complex() Returns a complex number
    # delattr() Deletes the specified attribute (property or method) from the specified object
    # divmod() Returns the quotient and the remainder when argument1 is divided by argument2
    # eval() Evaluates and executes an expression
    # exec() Executes the specified code (or object)
    # filter() Use a filter function to exclude items in an iterable object
    # format() Formats a specified value
    # frozenset() Returns a frozenset object
    # getattr() Returns the value of the specified attribute (property or method)
    # globals() Returns the current global symbol table as a dictionary
    # hasattr() Returns True if the specified object has the specified attribute (property/method)
    # hash() Returns the hash value of a specified object
    # help() Executes the built-in help system
    # hex() Converts a number into a hexadecimal value
    # isinstance() Returns True if a specified object is an instance of a specified object
    # issubclass() Returns True if a specified class is a subclass of a specified object
    # iter() Returns an iterator object
    # locals() Returns an updated dictionary of the current local symbol table
    # map() Returns the specified iterator with the specified function applied to each item
    # memoryview() Returns a memory view object
    # next() Returns the next item in an iterable
    # object() Returns a new object
    # oct() Converts a number into an octal
    # pow() Returns the value of x to the power of y
    # property() Gets, sets, deletes a property
    # repr() Returns a readable version of an object
    # reversed() Returns a reversed iterator
    # round() Rounds a numbers
    # setattr() Sets an attribute (property/method) of an object
    # slice() Returns a slice object
    # sorted() Returns a sorted list
    # @staticmethod() Converts a method into a static method
    # super() Returns an object that represents the parent class
    # vars() Returns the __dict__ property of an object
    # zip() Returns an iterator, from two or more iterators


if __name__ == "__main__":
    main()
