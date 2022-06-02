
def bubbleSort(array):
    # TODO
    n = len(array)
    # TODO
    for i in range(n - 1):
        # TODO
        for j in range(0, n - i - 1):
            # TODO
            if array[j] > array[j + 1]:
                # TODO
                array[j], array[j + 1] = array[j + 1], array[j]
