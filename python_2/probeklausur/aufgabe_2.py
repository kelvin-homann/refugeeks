# Exceptions sind Fehler die in Python das Programm zum Abstürzen bringen können
# Exceptions können aber auch mit try/except behandelt werden damit das Programm nicht abstürzt
# Um eigene Exceptions zu schreiben muss eine eigene Klasse von Exception erben und die __str__ Methode den Fehler zurückgeben

class ExampleError(Exception):
    def __str__(self) -> str:
        return "Es ist ein Fehler aufgetreten!"
