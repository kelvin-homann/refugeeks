class Circle:
    PI = 3.1415

    def __init__(self, radius):
        self.__radius = radius

    def getRadius(self):
        return self.__radius

    def setRadius(self, radius):
        self.__radius = radius

    def getFlaeche(self):
        return round(self.PI * self.__radius ** 2, 2)

    def getUmfang(self):
        return round(self.PI * 2 * self.__radius, 2)


kreis1 = Circle(12)
print("Radius: ", kreis1.getRadius())
print("Umfang: ", kreis1.getUmfang())
print("Fläche: ", kreis1.getFlaeche())

kreis2 = Circle(20)
print("Radius: ", kreis2.getRadius())
print("Umfang: ", kreis2.getUmfang())
print("Fläche: ", kreis2.getFlaeche())


# kreise = [Circle(5), Circle(8)]

# for kreis in kreise:
#     print("Radius: ", kreis.getRadius())
#     print("Umfang: ", kreis.getUmfang())
#     print("Fläche: ", kreis.getFlaeche())
