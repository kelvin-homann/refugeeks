my_list = [24, 10, 12, 89]


def insertIntoList(index, item, liste):
    try:
        liste[index] = item
    except IndexError:
        print("Der Index {} befindet sich außerhalb der Liste".format(index))

    return liste


# alternative: Hier müssen wir den Fehler selber werfen


def insertIntoList2(index, item, liste):
    if (index > len(liste) - 1):
        raise IndexError

    liste.insert(index, item)

    return liste


my_list = insertIntoList(2, 15, my_list)
my_list = insertIntoList(10, 15, my_list)
print(my_list)

try:
    my_list = insertIntoList2(10, 15, my_list)
except IndexError:
    print("Der Index befindet sich außerhalb der Liste")
