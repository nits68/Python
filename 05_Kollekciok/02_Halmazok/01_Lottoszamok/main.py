import random
from typing import List, Set

# Elöltesztelő ciklus példa: lottószámok generálása
lotto90: Set[int] = set()  # Halmaz
while len(lotto90) < 5:
    lotto90.add(random.randint(1, 90))  # 1 >= vélszám <= 90
print(lotto90)

# Halmaz elemei növekvő sorrendben tartalmazás vizsgálattal:
lotto90rendezve: List[int] = []
for i in range(1, 91):  # 1..90
    if i in lotto90:
        lotto90rendezve.append(i)
print(lotto90rendezve)
