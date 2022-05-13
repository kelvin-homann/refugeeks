
def divide(n):
    try:
        print(1/n)
    except ZeroDivisionError:
        print('Fehler: Division durch Null !!')


n = int(input("Bitte gib eine Zahl ein: "))
divide(n)
