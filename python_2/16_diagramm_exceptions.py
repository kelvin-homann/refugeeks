class DataValueToBigError(Exception):
    def __str__(self) -> str:
        return "Ein Value ist zu groß!"


class DataValueToSmallError(Exception):
    def __str__(self) -> str:
        return "Ein Value ist zu klein!"


class Diagramm:
    def __init__(self, title, data, min, max):
        self.min = min
        self.max = max
        self.data = data
        self.validate()

        self.title = title

    def getSpaces(self, word):
        longestKey = ''
        for key in self.data:
            if len(key) > len(longestKey):
                longestKey = key

        spaceBetween = len(longestKey) - len(word)

        return spaceBetween * ' '

    def validate(self):
        for key in self.data:
            if self.data[key] < self.min:
                raise DataValueToSmallError

            if self.data[key] > self.max:
                raise DataValueToBigError

    def printDiagramm(self):
        print(self.title)

        for key in self.data:
            spacesBetween = self.getSpaces(key)

            row = "{}{}: ".format(key, spacesBetween)

            for i in range(self.data[key]):
                row += '#'
            print(row)


data = {"Kelvin": 4, "Peter": 2, "Max": 1, "Ali": 3, "Gustav": 6}
diagramm = Diagramm("Noten Python 1", data, 1, 4)
diagramm.printDiagramm()
