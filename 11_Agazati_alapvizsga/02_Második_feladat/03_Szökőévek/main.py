def szökőév(év: int) -> bool:
    return év % 400 == 0 or év % 4 == 0 and év % 100 != 0


def main() -> None:
    # Kérjünk be a felhasználótól két évszámot!
    # Határozzuk meg és írjuk ki a képernyőre az
    # évszámok közötti szökőéveket!
    # A szökőév meghatározásához készítsünk saját függvényt!
    # Szökőév minden 400-al osztható év, illetve
    # a 4-el osztható, de 100-al nem osztható évek.
    # Ha a megadott évszámok között nem található
    # szökőév, akkor a "Nincs szökőév a megadott tartományban!" szöveget jelenítsük meg!
    print("2. feladat: Szökőév listázó")
    év1: int = int(input("Kérem az egyik évszámot: "))
    év2: int = int(input("Kérem a másik évszámot: "))
    tól_év: int = min(év1, év2)
    ig_év: int = max(év1, év2)
    szökőévek: list[str] = []
    for év in range(tól_év, ig_év + 1):
        if szökőév(év):
            szökőévek.append(str(év))
    if len(szökőévek) == 0:
        print("Nincs szökőév a megadott tartományban!")
    else:
        évek: str = "; ".join(szökőévek)
        print(f"Szökőévek: {évek}")


if __name__ == "__main__":
    main()
