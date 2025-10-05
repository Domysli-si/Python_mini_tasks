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
try:
    d.otevrit()
    print("Prosel jsem")
except ZamceneDvereException:
    print("Dvere jsou zamcene, nemuzes je otevrit")
