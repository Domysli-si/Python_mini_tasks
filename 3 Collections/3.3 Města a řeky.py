# Slovník řek: název → (prameniště, [seznam měst])
reky = {
    "Vltava": ("Černý Kříž", ["Vyšší Brod", "České Budějovice", "Praha"]),
    "Labe": ("Špindlerův Mlýn", ["Děčín", "Ústí nad Labem", "Litoměřice"]),
    "Morava": ("Králický Sněžník", ["Olomouc", "Uherské Hradiště", "Hodonín"])
}

# Vytvoření obráceného slovníku: město → seznam řek
mesto_do_rek = {}

for reka, (prameniste, mesta) in reky.items():
    for mesto in mesta:
        mesto_lower = mesto.lower()
        if mesto_lower not in mesto_do_rek:
            mesto_do_rek[mesto_lower] = []
        mesto_do_rek[mesto_lower].append(reka)

# Hlavní smyčka programu
while True:
    vstup = input("\nZadej název města nebo řeky (nebo 'konec' pro ukončení): ").strip()

    if vstup.lower() == "konec":
        print("Program ukončen.")
        break

    vstup_lower = vstup.lower()

    # Zpracování jako název řeky
    if vstup.capitalize() in reky:
        prameniste, mesta = reky[vstup.capitalize()]
        print(f"\nŘeka {vstup.capitalize()} pramení v: {prameniste}")
        print("Protéká těmito místy:")
        for m in mesta:
            print(f" - {m}")

    # Zpracování jako název města
    elif vstup_lower in mesto_do_rek:
        reky_v_meste = mesto_do_rek[vstup_lower]
        print(f"\nMěstem {vstup} protéká tyto řeky:")
        for reka in reky_v_meste:
            print(f" - {reka}")
    else:
        print("Zadané město nebo řeka nebyly nalezeny. Zkontroluj překlep.")
