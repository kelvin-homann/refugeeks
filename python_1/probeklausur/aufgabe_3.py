# Konvertierung zu int war falsch
word = input('Welches Wort soll geprüft werden? ')


def greatestChar(long_word):
    maxChar = long_word[0]  # vorher 2.5, hat keinen Sinn gemacht
    for c in long_word:
        if c > maxChar:
            maxChar = c  # Hier war vorher maxChar = c vertauscht
        # else: break war falsch

    return maxChar  # return hat gefehlt


greatest_char = greatestChar(word)
