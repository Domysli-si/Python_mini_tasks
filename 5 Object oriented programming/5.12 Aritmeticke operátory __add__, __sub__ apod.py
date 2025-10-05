import re

class PenezniHotovost:
    def __init__(self, castka: float, mena: str):
        if not re.match(r"^[A-Z]{3}$", mena):
            raise Exception('Mena neodpovida formatu zapisu tri velkych pismen.')
        self._mena = mena
        self._castka = castka

    def __str__(self):
        return str(self._castka) + " " + self._mena

    def __add__(self, other):
        if isinstance(other, (float, int)):
            return PenezniHotovost(self._castka + other, self._mena)
        if isinstance(other, PenezniHotovost) and other._mena == self._mena:
            return PenezniHotovost(self._castka + other._castka, self._mena)
        raise Exception("Penezni hotovost lze scitat pouze s int,float a hotovosti ve stejne mene")

    def __sub__(self, other):
        if isinstance(other, (float, int)):
            return PenezniHotovost(self._castka - other, self._mena)
        if isinstance(other, PenezniHotovost) and other._mena == self._mena:
            return PenezniHotovost(self._castka - other._castka, self._mena)
        raise Exception("Penezni hotovost lze odcitat pouze s int,float a hotovosti ve stejne mene")

    def __mul__(self, other):
        if isinstance(other, (float, int)):
            return PenezniHotovost(self._castka * other, self._mena)
        raise Exception("Penezni hotovost lze nasobit pouze int nebo float")

    def __pow__(self, power, modulo=None):
        if not isinstance(power, (int, float)):
            raise Exception("Exponent musi byt cislo int nebo float")
        result = self._castka ** power
        return PenezniHotovost(result, self._mena)

#tests
sto_korun = PenezniHotovost(100, "CZK")

print(sto_korun + 100)       
print(sto_korun - 30)        
print(sto_korun * 2)          
print(sto_korun ** 2)          

dve_sta_korun = sto_korun + 100
print(dve_sta_korun - sto_korun)  
