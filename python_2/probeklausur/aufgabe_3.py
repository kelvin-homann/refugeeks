class Person:
    def __init__(self, name, email) -> None:
        self.name = name
        self.email = email


class Student(Person):
    def __init__(self, name, email, id, durchschnittsnote) -> None:
        super().__init__(name, email)
        self.id = id
        self.durchschnittsnote = durchschnittsnote


class Lehrer(Person):
    def __init__(self, name, email, gehalt) -> None:
        super().__init__(name, email)
        self.gehalt = gehalt


class Seminar:
    def __init__(self, name, id) -> None:
        self.name = name
        self.id = id
        self.lehrer = None
        self.schuelerListe = []

    def meldeSchuelerAn(self, schueler):
        self.schuelerListe.append(schueler)

    def setLehrer(self, lehrer):
        self.lehrer = lehrer


seminar = Seminar("Python 2", 1)
lehrer = Lehrer("Kelvin", "kelvin@mail.de", 10)
student = Student("Max", "max@mail.de", 1, 2)

seminar.meldeSchuelerAn(student)
seminar.setLehrer(lehrer)
