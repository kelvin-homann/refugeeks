
def calculateAreaForCircle(radius):
    return 3.1415 * radius ** 2


def calculateAreaForSquare(length):
    return length ** 2


def calculateAreaForRectangle(length, depth):
    return length * depth


def printResult(figure, area):
    print("Die Fläche vom", figure, "ist", round(area, 2), "cm^2")


def promptUserInput():
    figure = input('Welche geometrischen Figur soll berechnet werden? ')

    if figure == 'Kreis':
        r = float(input('Eingabe Radius: '))
        circleArea = calculateAreaForCircle(r)
        printResult(figure, circleArea)

    elif figure == 'Quadrat':
        a = float(input('Eingabe a: '))
        squareArea = calculateAreaForSquare(a)
        printResult(figure, squareArea)

    elif figure == 'Rechteck':
        a = float(input('Eingabe a: '))
        b = float(input('Eingabe b: '))
        rectangleArea = calculateAreaForRectangle(a, b)
        printResult(figure, rectangleArea)

    else:
        print('Diese Figur kenne ich nicht!')


promptUserInput()
