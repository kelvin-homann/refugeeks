# Schreibt eine Funktion, welche für einen gegebenen Monat,
# die Anzahl der Tage in diesem Monat zurückgibt.
# (Für den Februar soll immer 28 zurückgegeben werden.)

# Nutzt einen Dictionary um diese Aufgabe zu lösen.


def getDaysFromMonth(month):
    months = {
        "january": {
            "days": 31
        },
        "february": {
            "days": 28
        },
        "march": {
            "days": 31
        },
        "april": {
            "days": 30
        },
        "may": {
            "days": 31
        },
        "june": {
            "days": 30
        },
        "july": {
            "days": 31
        },
        "august": {
            "days": 31
        },
        "september": {
            "days": 30
        },
        "october": {
            "days": 31
        },
        "november": {
            "days": 30
        },
        "dezember": {
            "days": 31
        }
    }

    return months[month]["days"]


month = input("Von welchem Monat möchtest du die Anzahl der Tage wissen?: ")
print(getDaysFromMonth(month))
