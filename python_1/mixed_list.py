# Schreibt eine Funktion,
# welche alle Werte außer Integer Werten aus einem
# gegebenen Array mit gemischten Werten zu entfernen.

random_list = [23.83, 62, -3.8, 'Python', 0, 'Refugeeks', 26]


def removeNonIntegerFromList(mixed_list):
    int_list = []
    for i in mixed_list:
        if type(i) == int:
            int_list.append(i)

    return int_list


print(removeNonIntegerFromList(random_list))
