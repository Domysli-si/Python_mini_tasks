import math  # Na výpočet π a druhé mocniny

# Funkce pro výpočet obsahu kruhu
def obsah_kruhu(r):
    if r <= 0:
        # Pokud je poloměr záporný nebo nulový, vyhodíme výjimku ArithmeticError
        raise ArithmeticError("Poloměr musí být kladné číslo.")
    # Výpočet obsahu: π * r^2
    return math.pi * r ** 2

# Načítání vstupu s ošetřením chyb
while True:
    try:
        vstup = input("Zadej poloměr kruhu: ")
        polomer = float(vstup)  # Převedeme vstup na desetinné číslo
        obsah = obsah_kruhu(polomer)  # Zavoláme naši funkci
        print(f"Obsah kruhu je: {obsah:.2f}")  # Výstup zaokrouhlený na 2 desetinná místa
        break  # Konec smyčky, pokud vše proběhlo správně
    except ValueError:
        print("Zadal jsi neplatnou hodnotu. Zadej prosím číslo.")
    except ArithmeticError as e:
        print("Chyba:", e)
