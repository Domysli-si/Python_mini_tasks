# Neustále se ptáme uživatele, dokud nezadá platné číslo
while True:
    x = input("Zadej číslo: ")
    try:
        # Pokusíme se převést vstup na celé číslo
        y = int(x) + 1
        # Pokud převod proběhne úspěšně, ukončíme smyčku
        break
    except ValueError:
        # Pokud dojde k chybě (např. uživatel zadá písmena), zobrazíme chybovou hlášku
        print("Nezadal jsi platné číslo. Zkus to znovu.")

# Vytiskneme výsledek
print("Zadané číslo + 1 je:", y)
