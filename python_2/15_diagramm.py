class Diagramm:
    def __init__(self, title, data):
        self.title = title
        self.data = data

    def getSpaces(self, word):
        # Schritt 1:
        laengstes_wort = ''

        for key in self.data:
            if len(key) > len(laengstes_wort):
                laengstes_wort = key

        # Schritt 2:
        abstand = len(laengstes_wort) - len(word)

        # Schritt 3:
        return abstand * ' '

    def printDiagramm(self):
        print(self.title)

        for key in self.data:
            spaces = self.getSpaces(key)
            row = "{}{}: {}".format(key, spaces, self.data[key] * '#')

            # alternative
            # for i in range(self.data[key]):
            #     row += '#'
            print(row)


data = {"Kelvin": 4, "Peter": 2, "Max": 2, "Ali": 3, "Gustav": 6}
diagramm = Diagramm("Noten Python 1", data)
diagramm.printDiagramm()
