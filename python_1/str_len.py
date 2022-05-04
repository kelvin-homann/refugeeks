# Schreibt eine Funktion, welche eine Liste
# von Wörtern annimmt und das längste Wort
# und die Länge des längsten Wortes zurückgibt.

def getLongestWordFromList(word_list):
    longest_word = ""
    for i in word_list:
        if len(i) > len(longest_word):
            longest_word = i

    return longest_word, len(longest_word)


list_with_many_words = ["Refugeeks", "Python", "Kelvin", "Hochschule Hannover"]

word, length = getLongestWordFromList(list_with_many_words)

print("Das Längste Wort in der Liste ist", word,
      "mit einer Länge von", length, "Charakteren!")
