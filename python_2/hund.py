class Hund:
    def __init__(self, name, gewicht):
        self.name = name
        self.gewicht = gewicht

    def bellen(self):
        print("Woof Woof 🐶")


hund = Hund("Gustav", 15)

hund.bellen()
