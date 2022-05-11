class Auto:
    def __init__(self, preis):
        self.preis = preis


audi = Auto(15000)
print(audi.preis)
audi.preis = 20000
print(audi.preis)
