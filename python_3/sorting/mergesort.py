def merge(liste, linkeListe, rechteListe):
    indexLinkeListe = indexRechteListe = indexListe = 0

    while indexLinkeListe < len(linkeListe) and indexRechteListe < len(rechteListe):
        if linkeListe[indexLinkeListe] <= rechteListe[indexRechteListe]:
            liste[indexListe] = linkeListe[indexLinkeListe]
            indexLinkeListe += 1
        else:
            liste[indexListe] = rechteListe[indexRechteListe]
            indexRechteListe += 1
        indexListe += 1

    while indexLinkeListe < len(linkeListe):
        liste[indexListe] = linkeListe[indexLinkeListe]
        indexLinkeListe += 1
        indexListe += 1

    while indexRechteListe < len(rechteListe):
        liste[indexListe] = rechteListe[indexRechteListe]
        indexRechteListe += 1
        indexListe += 1


def merge_sort(liste):
    if len(liste) < 2:  # Abbruchbedingung, um die Rekursion beenden zu können
        return liste
    mitte = len(liste) // 2

    linkeListe = liste[:mitte]
    rechteListe = liste[mitte:]

    merge_sort(linkeListe)
    merge_sort(rechteListe)

    return merge(liste, linkeListe, rechteListe)
