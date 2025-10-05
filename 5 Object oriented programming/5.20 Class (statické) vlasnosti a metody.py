class KonfiguraceKonference:

    _maximalni_pocet_ucastniku = 0

    def __new__(cls, *args, **kwargs):
        raise Exception("Není dovoleno vytvářet instance této třídy!")

    @classmethod
    def set_maximalni_pocet_ucastniku(cls, max):
        cls._maximalni_pocet_ucastniku = max

    @classmethod
    def get_maximalni_pocet_ucastniku(cls):
        return cls._maximalni_pocet_ucastniku


print(KonfiguraceKonference.get_maximalni_pocet_ucastniku())  # 0

KonfiguraceKonference.set_maximalni_pocet_ucastniku(212)
print(KonfiguraceKonference.get_maximalni_pocet_ucastniku())  # 212

