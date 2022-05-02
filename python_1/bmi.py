
height = float(input('Bitte gib deine Korpergröße in m ein: '))
weight = int(input('Bitte gib dein Gewicht in kg ein: '))
bmi = round((weight / (height * height)), 1)

if bmi < 19.0:
    print('Du hast Untergewicht')
elif 19.0 < bmi < 24.9:
    print('Du hast Normalgewicht')
elif bmi > 25.0:
    print('Du hast Übergewicht')
