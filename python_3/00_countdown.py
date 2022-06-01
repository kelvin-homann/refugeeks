def countdown(n):
    print(n)
    if n == 1 or n == 0:  # Abbruchbedingung
        return
    else:
        countdown(n - 1)  # Funktion ruft sich selbst auf


countdown(10)
