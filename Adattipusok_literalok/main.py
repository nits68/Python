# Az adattípus meghatározza a változóban tárolható értékek számát, típusát és értéktartományát
# Változó: Egy vagy több érték tárolására használt egység
# Változók jellemzői: adattípus, azonosító (név), kezdőérték, aktuális érték
# A literál olyan adat, melyhez nem rendelünk azonosítót, a megadás szintaxisa határozza meg a típusát

# 1. Egyszerű adattípusok: Egy érték tárolására alkalmasak
# 1.1 Szöveges adattípus és literál: str
szöveg: str = "Python"
szöveg2: str = 'Jedlik'
print(type(szöveg))

# 1.2 Numerikus adattípusok: int, float, complex és a literálok
egész: int = 68
valós: float = 3.14
komplex: complex = 3j
print(type(egész))
print(type(valós))
print(type(komplex))

# 1.3 Logikai adattípus: bool
logikai: bool = True  # Értéke csak True vagy False lehet

# 2. Összetett adattípusok: Több érték tárolását teszik lehetővé
lista = ["apple", "banana", "cherry"]
print(lista)
x = ["apple", "banana", "cherry"]	list	
x = ("apple", "banana", "cherry")	tuple	
# x = range(6)
# x = {"name" : "John", "age" : 36}	dict	
# x = {"apple", "banana", "cherry"}	set	
# x = frozenset({"apple", "banana", "cherry"})	frozenset	
# x = True	bool	
# x = b"Hello"		
# x = bytearray(5)	
# x = memoryview(bytes(5))
