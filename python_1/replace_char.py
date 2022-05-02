word = input("Bitte gib ein Wort ein: ")
character = input("Welcher Buchstabe soll ersetzt werden?: ")
replacement = input("Womit soll der Buchstabe ersetzt werden?: ")

new_word = ''
for char in word:
    if char == character:
        new_word += replacement
    else:
        new_word += char

print("Das neue Wort ist: ", new_word)
