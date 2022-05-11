class Kunde:
    def __init__(self, id, kontostand) -> None:
        self.id = id
        self.kontostand = kontostand


class PrivatKunde(Kunde):
    def __init__(self, id, kontostand, vorname) -> None:
        super().__init__(id, kontostand)
        self.vorname = vorname

    def __str__(self) -> str:
        return "{} hat {}€ auf dem Konto.".format(self.vorname, self.kontostand)


kelvin = PrivatKunde(1, 100, "Kelvin")
print(kelvin)
