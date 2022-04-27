# Schreibt ein Programm, das für eine beliebige Anzahl von Zahlen deren Durchschnitt berechnet.

# Dazu soll erst die Anzahl der Zahlen eingegeben werden, im Anschluss werden entsprechend viel
# Zahlen eingegeben und der der Durchschnitt angezeigt. Ein möglicher Ablauf ist wie folgt:

x = int(input("Bitte gib eine Breite an: "))
y = int(input("Bitte gib eine Tiefe an: "))

s = "*"
for i in range(y):
    print(s * x)
