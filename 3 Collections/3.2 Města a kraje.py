# Slovník: kraje jako klíče, seznam měst jako hodnoty
mapa_cr = {
    "Jihomoravský kraj": ["Brno", "Znojmo", "Hodonín", "Břeclav", "Vyškov"],
    "Moravskoslezský kraj": ["Ostrava", "Opava", "Karviná", "Frýdek-Místek", "Třinec"],
    "Středočeský kraj": ["Kladno", "Mladá Boleslav", "Příbram", "Kolín", "Kutná Hora"]
}

# Vytvoříme obrácený slovník: město → kraj
mesto_do_kraje = {}
for kraj, mesta in mapa_cr.items():
    for mesto in mesta:
        mesto_do_kraje[mesto.lower()] = kraj  # ukládáme v lowercase pro lepší porovnání

# Hlavní smyčka programu
while True:
    vstup = input("\nZadej název města nebo kraje (nebo 'konec' pro ukončení): ").strip()

    if vstup.lower() == "konec":
        print("Program ukončen.")
        break

    # Zpracování vstupu jako město
    if vstup.lower() in mesto_do_kraje:
        kraj = mesto_do_kraje[vstup.lower()]
        print(f"Město {vstup} se nachází v kraji: {kraj}")

    # Zpracování vstupu jako kraj
    elif vstup in mapa_cr:
        mesta = mapa_cr[vstup]
        print(f"Kraj {vstup} obsahuje tato města: {', '.join(mesta)}")

    else:
        print("Neznámý název města nebo kraje. Zkontroluj překlep.")
