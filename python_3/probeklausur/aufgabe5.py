# Laufzeit von BubbleSort: O(n^2)

# die Funktion bubbleSort nimmt ein array als Parameter an
def bubbleSort(array):
    # wir holen uns die Länge der Liste
    n = len(array)
    # wir iterieren über das gesamte array bis auf das letzte Element
    for i in range(n - 1):
        # wir iterieren über den bisher nicht sortierten teilbereich der Liste
        for j in range(0, n - i - 1):
            # Wir vergleichen zwei nebeneinander liegende Elemente im unsortierten Teilbereich der Liste
            if array[j] > array[j + 1]:
                # Wenn das linke Element größer ist als das rechte dann werden die Elemente getauscht
                array[j], array[j + 1] = array[j + 1], array[j]
