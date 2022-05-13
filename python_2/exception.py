# Auf Exception reagieren
try:
    input = int(input("Eine Zahl eingeben größer 0 eingeben: "))
    print(5 / input)
except ZeroDivisionError:
    print("Fehler: Durch 0 dividiert")

print("hallo")
