def promptInput():
    list_of_words = []
    print("Bitte gib die Wörter ein: ")
    while True:
        current_input = input(": ")

        if current_input == "END":
            break
        else:
            list_of_words.append(current_input)

    return list_of_words


def calculateAverage(words):
    n = len(words)
    sum_of_chars = 0

    for word in words:
        sum_of_chars += len(word)

    return round(sum_of_chars / n, 2)


words = promptInput()
print("Durchschnitt: ", calculateAverage(words))
