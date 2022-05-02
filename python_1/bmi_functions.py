
def promptInput():
    height = float(input('Bitte gib deine Korpergröße in m ein: '))
    weight = int(input('Bitte gib dein Gewicht in kg ein: '))

    return height, weight


def calculateBMI(height, weight):
    return round((weight / (height * height)), 1)


def interpretResult(bmi):
    if bmi < 19.0:
        print('Du hast Untergewicht')
    elif 19.0 < bmi < 24.9:
        print('Du hast Normalgewicht')
    elif bmi > 25.0:
        print('Du hast Übergewicht')


height, weight = promptInput()
bmi = calculateBMI(height, weight)
interpretResult(bmi)
