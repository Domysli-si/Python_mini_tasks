from datetime import datetime

try:
    # Načtení vstupních hodnot
    rok = int(input("Zadej rok narození: "))
    mesic = int(input("Zadej měsíc narození (1–12): "))
    den = int(input("Zadej den narození: "))

    # Kontrola roku
    aktualni_rok = datetime.now().year
    vek = aktualni_rok - rok
    if vek < 0 or vek > 119:
        raise Exception("Chyba: Rok musí být nastaven tak, aby člověku bylo mezi 0 a 119 lety.")

    # Kontrola měsíce
    if mesic < 1 or mesic > 12:
        raise Exception("Chyba: Měsíc musí být číslo od 1 do 12.")

    # Kontrola dne dle měsíce
    if mesic in [1, 3, 5, 7, 8, 10, 12]:
        max_den = 31
    elif mesic == 2:
        max_den = 29  # Přestupný rok ignorujeme
    else:
        max_den = 30

    if den < 1 or den > max_den:
        raise Exception(f"Chyba: Den pro měsíc {mesic} musí být mezi 1 a {max_den}.")

    # Kontrola letních prázdnin (červenec = 7, srpen = 8)
    if mesic in [7, 8]:
        raise Exception(f"Nepovolené datum: {den}.{mesic}.{rok} spadá do letních prázdnin.")

    # Pokud všechno projde
    print(f"Zadané datum narození je platné: {den}.{mesic}.{rok}")

except Exception as e:
    # Výpis chyby
    print(e)
