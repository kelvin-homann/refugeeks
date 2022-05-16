def writeIntoFile(string):
    try:
        file = open("strings.txt", "a")
        file.write(string)
        file.close()
    except FileNotFoundError:
        print("Die Datei existiert nicht")
        open("strings.txt", "x")  # Optional


user_input = input("Was soll in die Datei eingefügt werden?")
writeIntoFile(user_input)
