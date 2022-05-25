import time
import random


def bubbleSort(my_list):
    n = len(my_list)

    for i in range(n - 1):
        print(n, i, n - i - 1)
        for j in range(0, n - i - 1):
            if my_list[j] > my_list[j + 1]:
                my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]


my_list = [2, 25, 12, 52, 10]
# my_list = random.sample(range(0, 9999), 8800)
# my_list_new = my_list

# startBubble = time.time()
bubbleSort(my_list)
# endBubble = time.time()

# startPython = time.time()
# my_list_new.sort()
# endPython = time.time()

# print("{} {}".format((endBubble-startBubble)
#       * 1000, (endPython-startPython) * 1000))
