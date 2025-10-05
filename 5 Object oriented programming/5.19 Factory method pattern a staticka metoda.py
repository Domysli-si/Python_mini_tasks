class Firma:

    @staticmethod
    def factory_from_obchodni_nazev(obchodni_nazev: str):
        casti = obchodni_nazev.rsplit(",", 1)
        if len(casti) != 2:
            raise Exception("Nelze parsovat obchodni nazev")

        nazev = casti[0].strip()
        pravni_forma = casti[1].strip()
        return Firma(nazev, pravni_forma)

    def __init__(self, nazev, pravni_forma):
        self.jmeno = nazev
        self.pravni_forma = pravni_forma


sporka = Firma.factory_from_obchodni_nazev("Česká spořitelna, a.s.")
print(sporka.pravni_forma)  
