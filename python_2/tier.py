class Tier:
    def __init__(self, name, gewicht):
        self.name = name
        self.gewicht = gewicht

    def essen(self):
        print("{} isst etwas leckeres!".format(self.name))


class Vogel(Tier):
    def __init__(self, name, gewicht, art):
        super().__init__(name, gewicht)
        self.art = art

    def fliegen(self):
        print("{} fliegt hoch hinaus! 🦅".format(self.name))


class Fisch(Tier):
    def __init__(self, name, gewicht, art):
        super().__init__(name, gewicht)
        self.art = art

    def schwimmen(self):
        print("{} schwimmt in die Tiefe! 🐠".format(self.name))


forelle = Fisch("Rudolf", 1, "Forelle")
forelle.schwimmen()

adler = Vogel("Hans", 1, "Adler")
# adler.schwimmen() # Error
adler.fliegen()
