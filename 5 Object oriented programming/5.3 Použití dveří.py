class ZamceneDvereException(Exception):
    pass

class Dvere:
    def __init__(self, zamceno):
        self.zamceno = zamceno
    def otevrit(self):
        if self.zamceno:
            raise ZamceneDvereException
        return True

d = Dvere(zamceno=True)
prosel = False
try:
    d.otevrit()
    print("Prosel jsem")
    prosel = True
except ZamceneDvereException:
    print("Dvere jsou zamcene, nemuzes je otevrit")
finally:
    print("Uzivatel prosel dvermi:", prosel)
