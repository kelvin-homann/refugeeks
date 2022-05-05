def buchstabenErsetzen(wort, buchstabe, zeichen):
    neues_wort = ''
    for w in wort:
        if w == buchstabe:
            neues_wort += zeichen
        else:
            neues_wort += w

    return neues_wort


print(buchstabenErsetzen("refugeeks", "e", "#"))
