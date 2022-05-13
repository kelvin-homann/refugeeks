def getIndexOfChar(char):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    return alphabet.index(char) + 1


def convertStringToDict(string):
    my_dict = {}
    for char in string:
        my_dict[char] = getIndexOfChar(char)

    return my_dict


my_str = input("Welcher String soll konvertiert werden?: ")
print(convertStringToDict(my_str))
