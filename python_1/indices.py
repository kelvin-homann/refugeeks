# Schreibt eine Funktion, welche die Indizes der Elemente
# einer gegebenen Liste findet, die größer als ein bestimmter
# Wert sind.

def indicesOfList(original_list, big_value):
    indices = []

    for i in range(len(original_list)):
        if original_list[i] > big_value:
            indices.append(i)

    return indices


my_list = [1234, 1522, 1984, 19372, 1000, 2342, 7626]

print(indicesOfList(my_list, 3000))
