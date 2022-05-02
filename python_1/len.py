# Entwerft ein Programm, welches die Länge eines Strings ausgibt.
# Dabei soll natürlich nicht len() verwendet werden.

wort = input("Bitte gib ein Wort ein: ")
length = 0

for i in wort:
    length += 1

print("Der String hat eine Länge von: ", length)
