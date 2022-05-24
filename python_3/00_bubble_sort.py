def bubbleSort(array):
    n = len(array)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]


my_list = [5, 3, 1, 8, 10]
bubbleSort(my_list)
print(my_list)
