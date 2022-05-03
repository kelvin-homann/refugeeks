word = input('Welches Wort soll geprüft werden? ')


def greatestChar(long_word):
    maxChar = long_word[0]
    for c in long_word:
        if c > maxChar:
            maxChar = c
    return maxChar


greatest_char = greatestChar(word)
print("Der größte Buchstabe ist: ", greatest_char)
