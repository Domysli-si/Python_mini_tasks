from math import sqrt

while True:
    try:
        # Zadávání indukčnosti s kontrolou na číslo
        while True:
            try:
                L = float(input("Zadej indukčnost [H]: "))
                break
            except ValueError:
                print("Nezadal jsi číslo. Zadej prosím indukčnost znovu.")

        # Zadávání kapacity s kontrolou na číslo
        while True:
            try:
                C = float(input("Zadej kapacitu [F]: "))
                break
            except ValueError:
                print("Nezadal jsi číslo. Zadej prosím kapacitu znovu.")

        # Pokus o výpočet – může selhat, pokud L * C je záporné
        F = 1 / (2 * 3.14 * sqrt(L * C))

        # Pokud vše proběhlo v pořádku, vypíšeme výsledek a ukončíme smyčku
        print("Frekvence je: " + str(F) + " Hz")
        break

    except ValueError:
        # Toto zachytí chybu sqrt(záporné číslo)
        print("Chyba: Došlo k odmocnění záporného čísla.")
        print("Zadej prosím hodnoty L a C znovu.\n")
