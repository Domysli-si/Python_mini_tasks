import math
import cmath  # Pro komplexní odmocnění

# Načtení hodnot a, b, c s ošetřením vstupu
while True:
    try:
        a = float(input("Zadej a (nesmí být 0): "))
        if a == 0:
            print("a nesmí být 0, protože nejde o kvadratickou rovnici.")
            continue
        b = float(input("Zadej b: "))
        c = float(input("Zadej c: "))
        break
    except ValueError:
        print("Zadal jsi neplatnou hodnotu. Zkus to znovu.")

# Inicializace proměnných pro pozdější výpis ve finally
x1 = None
x2 = None
typ = ""

# Výpočet kvadratické rovnice s konstrukcí try-except-else-finally
try:
    D = b**2 - 4 * a * c  # Diskriminant
    # Pokus o výpočet odmocniny diskriminantu – pokud je záporný, vyvolá ValueError
    odmocnina = math.sqrt(D)
except ValueError:
    # Pokud dojde k pokusu o odmocnění záporného čísla, použijeme cmath
    odmocnina = cmath.sqrt(b**2 - 4 * a * c)
    x1 = (-b + odmocnina) / (2 * a)
    x2 = (-b - odmocnina) / (2 * a)
    typ = "komplexní"
else:
    # Pokud nedošlo k výjimce, pokračujeme s reálnými čísly
    x1 = (-b + odmocnina) / (2 * a)
    x2 = (-b - odmocnina) / (2 * a)
    typ = "reálné"
finally:
    print("\n--- Výsledek ---")
    if x1 is not None and x2 is not None:
        print(f"Kořeny rovnice jsou {typ} čísla:")
        print(f"x1 = {x1}")
        print(f"x2 = {x2}")
    else:
        print("Nepodařilo se spočítat kořeny.")
