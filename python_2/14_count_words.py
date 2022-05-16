def countWordOccurence(fileName):
    word_dict = {}
    try:
        file = open(fileName, "r")
        words = file.read().split(" ")

        for word in words:
            if word in word_dict:
                word_dict[word] += 1
            else:
                word_dict[word] = 1
    except FileNotFoundError:
        print("Diese Datei existiert nicht!")

    return word_dict


print(countWordOccurence("dummy.txt"))
