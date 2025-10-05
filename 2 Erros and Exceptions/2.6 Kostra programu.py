# Ohmův zákon: U = R * I
# Požadavek: Uživatel zadá dvě veličiny, třetí se dopočítá.

try:
    u_input = input("Zadej napětí [V] (nech prázdné, pokud neznáš): ")
    r_input = input("Zadej odpor [Ω] (nech prázdné, pokud neznáš): ")
    i_input = input("Zadej proud [A] (nech prázdné, pokud neznáš): ")

    # Převedeme zadané hodnoty na float, pokud byly zadány
    U = float(u_input) if u_input else None
    R = float(r_input) if r_input else None
    I = float(i_input) if i_input else None

    # Požadavek: pouze JEDNA z veličin smí chybět
    nezname = [v is None for v in (U, R, I)].count(True)

    if nezname != 1:
        raise ValueError("Musíte zadat právě dvě veličiny.")

    # Výpočet proudu: I = U / R
    if U is not None and R is not None and I is None:
        I = U / R
        print(f"Proud I je {I:.2f} A")

    # Výpočet napětí: U = R * I
    elif R is not None and I is not None and U is None:
        raise NotImplementedError("Výpočet napětí ještě není implementován.")

    # Výpočet odporu: R = U / I
    elif U is not None and I is not None and R is None:
        raise NotImplementedError("Výpočet odporu ještě není implementován.")

except ValueError as ve:
    print("Chyba:", ve)
except NotImplementedError as nie:
    print("Neimplementováno:", nie)
except Exception as e:
    print("Neočekávaná chyba:", e)
