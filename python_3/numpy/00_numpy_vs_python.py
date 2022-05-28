import numpy as np
from time import time


def numpy_append():
    arr = np.empty((1, 0), int)
    for i in range(100000):
        arr = np.append(arr, np.array(i))


def list_append():
    list_1 = []
    for i in range(100000):
        list_1.append(i)


def compareAppendTimes():
    startTimeNumpy = time()
    numpy_append()
    endTimeNumpy = time()

    numpy_time = endTimeNumpy - startTimeNumpy
    print("Append (Numpy) : {}".format(endTimeNumpy - startTimeNumpy))
    startTimePython = time()
    list_append()
    endTimePython = time()

    python_time = endTimePython - startTimePython
    print("Append (Python): {}".format(endTimePython - startTimePython))

    print("Numpy-Arrays sind ca. {}ms langsamer als Python Listen und sind damit {}x langsamer.".format(
        round((numpy_time - python_time) * 1000, 2), round(numpy_time/python_time, 2)))


def compareMeanTimes():
    numpy_array = np.random.rand(1000000)
    list_conv = list(numpy_array)

    startTimeNumpy = time()
    numpy_mean = np.mean(numpy_array)
    endTimeNumpy = time()

    print("Durchschnitt berechnet von numpy: {}".format(numpy_mean))
    numpy_time = endTimeNumpy - startTimeNumpy

    print("Laufzeit (Numpy): {}".format(numpy_time))

    startTimePython = time()
    list_mean = np.mean(list_conv)
    endTimePython = time()

    print("Durchschnitt berechnet von Standard-Python: {}".format(list_mean))

    python_time = endTimePython - startTimePython
    print("Laufzeit (Python): {}".format(python_time))

    print("Numpy-Arrays sind ca. {}ms schneller als Python Listen und sind damit {}x schneller.".format(
        round((python_time - numpy_time) * 1000, 2), round(python_time/numpy_time, 2)))


print('--------------------------')
compareMeanTimes()
print('--------------------------')
compareAppendTimes()
print('--------------------------')
