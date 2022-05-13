class GeometrieRechner:
    figur = None

    def setFigur(self):
        figur = input("Welche figur soll berechnet werden? ")
        if figur == 'Kreis':
            self.figur = Kreis()
        elif figur == 'Quadrat':
            self.figur = Quadrat()
        elif figur == 'Rechteck':
            self.figur = Rechteck()
        else:
            print('Diese Figur kenne ich nicht!')

    def getFlaeche(self):
        return self.figur.getFlaeche()

    def getUmfang(self):
        return self.figur.getUmfang()


class Kreis:
    PI = 3.1415

    def __init__(self):
        self.setValues()

    def getRadius(self):
        return self.__radius

    def setValues(self):
        self.__radius = float(input("radius: "))

    def getFlaeche(self):
        return round(self.PI * self.__radius ** 2, 2)

    def getUmfang(self):
        return round(self.PI * 2 * self.__radius, 2)


class Rechteck:
    def __init__(self):
        self.setValues()

    def setValues(self):
        self.__a = float(input("a: "))
        self.__b = float(input("b: "))

    def getA(self):
        return self.__a

    def getB(self):
        return self.__b

    def getFlaeche(self):
        return round(self.__a * self.__b, 2)

    def getUmfang(self):
        return round((self.__a * 2) + (self.__b * 2), 2)


class Quadrat:
    def __init__(self):
        self.setValues()

    def setValues(self):
        self.__a = float(input("a: "))

    def getA(self):
        return self.__a

    def getFlaeche(self):
        return round(self.__a * self.__a, 2)

    def getUmfang(self):
        return round(self.__a * 4, 2)


rechner = GeometrieRechner()

rechner.setFigur()
print("Fläche:", rechner.getFlaeche())
print("Umfang:", rechner.getUmfang())
