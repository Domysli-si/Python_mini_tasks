reky = {
    "Vltava": {
        "pramen": "Černý Kříž",
        "mesta": ["Vyšší Brod", "České Budějovice", "Praha"],
        "usti_do": "Labe",
        "misto_usti": "Mělník",
        "pokracuje": False
    },
    "Berounka": {
        "pramen": "Západní Čechy (Mže + Radbuza)",
        "mesta": ["Beroun", "Praha"],
        "usti_do": "Vltava",
        "misto_usti": "Praha",
        "pokracuje": False
    },
    "Labe": {
        "pramen": "Špindlerův Mlýn",
        "mesta": ["Děčín", "Ústí nad Labem", "Litoměřice", "Mělník"],
        "usti_do": "Severní moře",
        "misto_usti": "Cuxhaven (DE)",
        "pokracuje": True
    },
    "Morava": {
        "pramen": "Králický Sněžník",
        "mesta": ["Olomouc", "Uherské Hradiště", "Hodonín", "Lužice"],
        "usti_do": "Dunaj",
        "misto_usti": "Bratislava",
        "pokracuje": False
    },
    "Svratka": {
        "pramen": "Žďárské vrchy",
        "mesta": ["Brno", "Pohořelice"],
        "usti_do": "Dyje",
        "misto_usti": "Pohořelice",
        "pokracuje": False
    },
    "Dyje": {
        "pramen": "Moravské pole",
        "mesta": ["Znojmo", "Lužice"],
        "usti_do": "Morava",
        "misto_usti": "Lužice",
        "pokracuje": False
    }
}

from collections import deque, defaultdict

# Vytvoření neorientovaného grafu: místo → seznam sousedů (míst)
graph = defaultdict(list)

# Pomocná funkce pro spojení dvou míst v grafu
def spoj(misto1, misto2):
    graph[misto1].append(misto2)
    graph[misto2].append(misto1)

# Naplnění grafu
for reky_nazev, data in reky.items():
    body = [data["pramen"]] + data["mesta"] + [data["misto_usti"]]
    for i in range(len(body)-1):
        spoj(body[i], body[i+1])

# BFS pro hledání cesty mezi místy
def najdi_trasu(start, cil):
    if start not in graph or cil not in graph:
        return None

    queue = deque([start])
    visited = {start: None}  # slovník: místo → předchůdce v cestě

    while queue:
        aktualni = queue.popleft()
        if aktualni == cil:
            # Rekonstruuj cestu
            cesta = []
            while aktualni is not None:
                cesta.append(aktualni)
                aktualni = visited[aktualni]
            return cesta[::-1]  # obráceně
        for soused in graph[aktualni]:
            if soused not in visited:
                visited[soused] = aktualni
                queue.append(soused)
    return None

# Funkce pro určení, po které řece se mezi dvěma místy pluje
def reky_na_trase(trasa):
    vysledek = []
    for i in range(len(trasa)-1):
        u = trasa[i]
        v = trasa[i+1]
        nalezena_reka = None
        for r, data in reky.items():
            body = [data["pramen"]] + data["mesta"] + [data["misto_usti"]]
            # Zkontrolujeme, zda u a v jsou sousední místa na této řece
            for j in range(len(body)-1):
                if (body[j] == u and body[j+1] == v) or (body[j] == v and body[j+1] == u):
                    nalezena_reka = r
                    break
            if nalezena_reka:
                break
        vysledek.append((u, v, nalezena_reka))
    return vysledek

# Hlavní program
while True:
    start = input("\nZadej výchozí místo (pramen/město): ").strip()
    if start.lower() == "konec":
        break
    cil = input("Zadej cílové místo (pramen/město): ").strip()
    if cil.lower() == "konec":
        break

    trasa = najdi_trasu(start, cil)
    if trasa is None:
        print("Cesta mezi zadanými místy nebyla nalezena.")
    else:
        print(f"\nTrasa z {start} do {cil}:")
        reky_trasa = reky_na_trase(trasa)
        for u, v, r in reky_trasa:
            print(f"  {u} → {v} po řece {r}")
