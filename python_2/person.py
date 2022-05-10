class Person:
    def __init__(self, name, groesse, gewicht):
        self.name = name
        self.groesse = groesse
        self.gewicht = gewicht

    def __str__(self):
        return str(self.name) + ' | ' + str(self.groesse) + 'm ' + str(self.gewicht) + 'kg'

    def getBMI(self):
        return round((self.gewicht / (self.groesse * self.groesse)), 1)


joe = Person("Joe", 1.8, 90)
print(joe)
print(joe.getBMI())
