class Buecherei:
    def __init__(self, ort, buecher) -> None:
        self.ort = ort
        self.buecher = buecher

    def ausleihen(self, buch, kunde):
        # bookIndex = self.buecher.index(buch)
        # self.buecher.pop(bookIndex)
        self.buecher.remove(buch)
        kunde.ausleihen(buch)


class Kunde:
    def __init__(self, name) -> None:
        self.name = name
        self.ausgeliehen = []

    def ausleihen(self, buch):
        self.ausgeliehen.append(buch)


class Buch:
    def __init__(self, titel, autor, seiten) -> None:
        self.titel = titel
        self.autor = autor
        self.seiten = seiten

    def __str__(self) -> str:
        return "{} von {}".format(self.titel, self.autor)


buch1 = Buch("Mathematik Grundlagen", "Pythagoras", 315)
buch2 = Buch("Physik für Anfänger", "Albert Einstein", 1050)
buch3 = Buch("Ein toller Roman", "Sybille Berg", 600)


buecherei = Buecherei("Hannover", [buch1, buch2, buch3])

print("----------------------")
for buch in buecherei.buecher:
    print(buch)

kunde1 = Kunde("Kelvin")

buecherei.ausleihen(buch2, kunde1)


print("----------------------")
for buch in buecherei.buecher:
    print(buch)

print("----------------------")
for buch in kunde1.ausgeliehen:
    print(buch)
