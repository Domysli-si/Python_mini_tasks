import re

class BankovniUcet:
    def __init__(self, cislo_uctu: str, mena: str):
        if not re.match(r"^[0-9]{5,10}/[0-9]{4}$", cislo_uctu):
            raise Exception('Cislo uctu neodpovida formatu zapisu 000000000/0000.')
        if not re.match(r"^[A-Z]{3}$", mena):
            raise Exception('Mena neodpovida formatu zapisu tri velkych pismen.')
        self._cislo_uctu = cislo_uctu
        self._mena = mena
        self._zustatek = 0

    def __str__(self):
        return f"{self._cislo_uctu}: {self._zustatek} {self._mena}"

    def __int__(self):
        return int(self._zustatek)

    def __float__(self):
        return float(self._zustatek)


ucet_alice = BankovniUcet("12341238/0100", "CZK")
print(ucet_alice)

zustatek_alice = int(ucet_alice)
print(zustatek_alice)
