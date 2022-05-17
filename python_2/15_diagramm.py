class Diagramm:
    def __init__(self, title, data):
        self.title = title
        self.data = data

    def printDiagramm(self):
        print(self.title)

        for key in self.data:
            row = "{}: {}".format(key, self.data[key] * '#')

            # alternative
            # for i in range(self.data[key]):
            #     row += '#'
            print(row)


data = {"Kelvin": 4, "Peter": 2, "Max": 2, "Ali": 3, "Gustav": 6}
diagramm = Diagramm("Noten Python 1", data)
diagramm.printDiagramm()
