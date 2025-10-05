import re

class PenezniHotovost:
    def __init__(self, castka: float, mena: str):
        if not re.match(r"^[A-Z]{3}$", mena):
            raise Exception('Mena neodpovida formatu zapisu tri velkych pismen.')
        self._mena = mena
        self._castka = castka

    def __str__(self):
        return f"{self._castka} {self._mena}"

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

    def __iadd__(self, other):
        if isinstance(other, (float, int)):
            self._castka += other
            return self
        if isinstance(other, PenezniHotovost) and other._mena == self._mena:
            self._castka += other._castka
            return self
        raise Exception("Penezni hotovost lze scitat pouze s int,float a hotovosti ve stejne mene")

    def __isub__(self, other):
        if isinstance(other, (float, int)):
            self._castka -= other
            return self
        if isinstance(other, PenezniHotovost) and other._mena == self._mena:
            self._castka -= other._castka
            return self
        raise Exception("Penezni hotovost lze odcitat pouze s int,float a hotovosti ve stejne mene")

    def __imul__(self, other):
        if isinstance(other, (float, int)):
            self._castka *= other
            return self
        raise Exception("Penezni hotovost lze nasobit pouze int nebo float")

    def __itruediv__(self, other):
        if isinstance(other, (float, int)):
            self._castka /= other
            return self
        if isinstance(other, PenezniHotovost) and other._mena == self._mena:
            self._castka /= other._castka
            return self
        raise Exception("Penezni hotovost lze delit pouze int,float a hotovosti ve stejne mene")

#tests
vyplata = PenezniHotovost(1000, "CZK")
vyplata += 2000
vyplata -= 500
vyplata *= 2
vyplata /= 2
print(vyplata) 
