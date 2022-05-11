class Auto:
    def __init__(self, marke, preis, model, baujahr):
        self.__marke = marke
        self.__preis = preis
        self.__model = model
        self.__baujahr = baujahr

    def __str__(self):
        return "Der {} {} aus dem Jahr {} kostet: {}€".format(self.__marke, self.__model, self.__baujahr, self.__preis)

    def setMarke(self, marke):
        self.__marke = marke

    def getMarke(self):
        return self.__marke

    def setPreis(self, preis):
        self.__preis = preis

    def getPreis(self):
        return self.__preis

    def setModel(self, model):
        self.__model = model

    def getModel(self):
        return self.__model

    def setBaujahr(self, baujahr):
        self.__baujahr = baujahr

    def getBaujahr(self):
        return self.__baujahr


audi_a5 = Auto("Audi", 30000, "A5", 2005)
mercedes_cls = Auto("Mercedes", 60000, "CLS", 2012)
ferrari = Auto("Ferrari", 260000, "812-competizione", 2022)

print(audi_a5)
print(mercedes_cls)

new_price = int(input("Bitte gib einen neuen Preis ein"))
ferrari.setPreis(new_price)
print(ferrari.getPreis())
