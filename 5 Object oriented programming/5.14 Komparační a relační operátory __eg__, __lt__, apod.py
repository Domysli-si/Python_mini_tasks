import re

class Zbozi:

    def __init__(self, nazev: str, vaha: float):
        if not re.match(r"^[\D ]{1,200}$", nazev):
            raise Exception('Nazev musi byt v rozsahu 1 az 200 znaku')
        if vaha <= 0:
            raise Exception('Vaha nesmi byt zapojna')

        self._nazev = nazev
        self._vaha = vaha

    def __lt__(self, other):
        if not isinstance(other, Zbozi):
            raise Exception('Porovnavat lze jen zbozi mezi sebou')
        return self._vaha < other._vaha

    def __gt__(self, other):
        if not isinstance(other, Zbozi):
            raise Exception('Porovnavat lze jen zbozi mezi sebou')
        return self._vaha > other._vaha

    def __le__(self, other):
        if not isinstance(other, Zbozi):
            raise Exception('Porovnavat lze jen zbozi mezi sebou')
        return self._vaha <= other._vaha

    def __ge__(self, other):
        if not isinstance(other, Zbozi):
            raise Exception('Porovnavat lze jen zbozi mezi sebou')
        return self._vaha >= other._vaha

    def __eq__(self, other):
        if not isinstance(other, Zbozi):
            return False
        return self._vaha == other._vaha

    def __ne__(self, other):
        if not isinstance(other, Zbozi):
            return True
        return self._vaha != other._vaha
