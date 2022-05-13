class BelowZeroError(Exception):
    def __str__(self) -> str:
        return "Der Radius ist kleiner als 0!"


class Kugel:
    def __init__(self, radius) -> None:
        if (radius < 0):
            raise BelowZeroError()
        else:
            self.radius = radius

    def getVolumen(self):
        return round(4/3 * 3.1415 * self.radius ** 3, 2)


try:
    kugel = Kugel(-1)
    print(kugel.getVolumen())
except BelowZeroError as error:
    print(error)

kugel = Kugel(5)
print(kugel.getVolumen())
