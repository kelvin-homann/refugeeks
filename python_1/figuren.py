# Entwerft ein Programm, dass die Fläche von geometrischen Figuren (Kreis, Quadrat, Rechteck) berechnet. Dazu soll die BenutzerIn
# die gewünschte Form (Kreis, Quadrat, Rechteck) eingeben
# die für diese erforderlichen Eingaben machen
# den Flächenwert ausgeben.

pi = 3.1415

figur = input('Welche geometrischen Figur soll berechnet werden? ')

if figur == ('Kreis'):
    r = float(input('Eingabe Radius: '))
    A = pi * r**2
    print('Die Fläche vom Kreis ist', round(A, 2), 'cm^2')

elif figur == ('Quadrat'):
    a = float(input('Eingabe a: '))
    B = a**2
    print('Die Fläche vom Quadrat ist', round(B, 2), 'cm^2')

elif figur == ('Rechteck'):
    s = float(input('Eingabe a: '))
    b = float(input('Eingabe b: '))
    C = s * b
    print('Die Fläche vom Rechteck ist', round(C, 2), 'cm^2')

else:
    print('Diese Figur kenne ich nicht!')
