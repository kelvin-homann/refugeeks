# Schreibe eine Funktion writeIntoFile(string),
# welche einen String als Parameter annimmt und diesen String in die Datei „strings.txt“ anfügt.

def writeIntoFile(string):
    file = open("strings.txt", 'a')
    file.write(string)
    file.close()
