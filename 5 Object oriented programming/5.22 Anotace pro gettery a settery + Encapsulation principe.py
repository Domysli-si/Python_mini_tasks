class Obdelnik:
    def __init__(self, sirka=0, vyska=0):
        self._sirka = 0
        self._vyska = 0
        self.sirka = sirka
        self.vyska = vyska

    @property
    def sirka(self):
        return self._sirka

    @sirka.setter
    def sirka(self, x):
        if x < 0:
            raise Exception("Šířka nesmí být záporná")
        self._sirka = x

    @property
    def vyska(self):
        return self._vyska

    @vyska.setter
    def vyska(self, x):
        if x < 0:
            raise Exception("Výška nesmí být záporná")
        self._vyska = x


# Test
obdelnik = Obdelnik(5, 10)
print(obdelnik.sirka, obdelnik.vyska)

obdelnik.sirka = 7
print(obdelnik.sirka)

# Toto vyhodí vyjimku
# obdelnik.vyska = -3
