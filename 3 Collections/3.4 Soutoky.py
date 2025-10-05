# Model 6 českých řek
reky = {
    "Vltava": {
        "pramen": "Černý Kříž",
        "usti_do": "Labe",
        "misto_usti": "Mělník",
        "pokracuje": False
    },
    "Berounka": {
        "pramen": "Západní Čechy (Mže + Radbuza)",
        "usti_do": "Vltava",
        "misto_usti": "Praha",
        "pokracuje": False
    },
    "Labe": {
        "pramen": "Špindlerův Mlýn",
        "usti_do": "Severní moře",
        "misto_usti": "Cuxhaven (DE)",
        "pokracuje": True
    },
    "Morava": {
        "pramen": "Králický Sněžník",
        "usti_do": "Dunaj",
        "misto_usti": "Bratislava",
        "pokracuje": False
    },
    "Svratka": {
        "pramen": "Žďárské vrchy",
        "usti_do": "Dyje",
        "misto_usti": "Pohořelice",
        "pokracuje": False
    },
    "Dyje": {
        "pramen": "Moravské pole",
        "usti_do": "Morava",
        "misto_usti": "Lužice",
        "pokracuje": False
    }
}

# Připravíme obrácený slovník: do které řeky se která vlévá
pritoky = {}

for nazev, data in reky.items():
    cilova_reka = data["usti_do"]
    if cilova_reka not in pritoky:
        pritoky[cilova_reka] = []
    pritoky[cilova_reka].append(nazev)

# Interaktivní dotazování
while True:
    vstup = input("\nZadej název řeky (nebo 'konec' pro ukončení): ").strip()

    if vstup.lower() == "konec":
        print("Program ukončen.")
        break

    if vstup not in reky:
        print("Řeka nenalezena. Zkontroluj překlep.")
        continue

    print(f"\n📍 Informace o řece: {vstup}")
    print(f" - Pramení v: {reky[vstup]['pramen']}")
    print(f" - Vlévá se do: {reky[vstup]['usti_do']} ({reky[vstup]['misto_usti']})")
    print(f" - Řeka po soutoku {'pokračuje' if reky[vstup]['pokracuje'] else 'zaniká'}.")

    # Najdi řeky, které se vlévají do této řeky
    pritekaji = pritoky.get(vstup, [])
    if pritekaji:
        print("\n🌊 Do této řeky se vlévají:")
        for r in pritekaji:
            print(f" - {r}")
    else:
        print("\n🌊 Do této řeky se nevlévá žádná jiná řeka v modelu.")
