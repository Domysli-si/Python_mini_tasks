

#otazka: Kdy se objekt maže?
class Zbozi1:
    def __init__(self, nazev):
        self.nazev = nazev

    def __del__(self):
        print("Zbozi " + str(self.nazev) + " bylo vymazano z pameti")

z = Zbozi1("Rohlik")
del z  


#otazka: Co se stane, když del z odstraníme a spustíme program?
class Zbozi2:
    def __init__(self, nazev):
        self.nazev = nazev

    def __del__(self):
        print("Zbozi " + str(self.nazev) + " bylo vymazano z pameti")

z = Zbozi2("Rohlik")
print("Konec programu")


#otazka: Co se stane, když máme dvě proměnné na jeden objekt?
class Zbozi3:
    def __init__(self, nazev):
        self.nazev = nazev

    def __del__(self):
        print("Zbozi " + str(self.nazev) + " bylo vymazano z pameti")

z = Zbozi3("Rohlik")
me_oblibene_zbozi = z

del z  
print("Po smazání proměnné z")

del me_oblibene_zbozi  
