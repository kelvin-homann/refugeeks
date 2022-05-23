import time
import random


def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid_point = (left + right) // 2
        if target < arr[mid_point]:
            right = mid_point - 1
        elif target > arr[mid_point]:
            left = mid_point + 1
        else:
            return mid_point

    return -1


def linear_search(my_list, x):
    for i in my_list:
        if i == x:
            return i

    return -1


randomlist = random.sample(range(1, 30000000), 1500000)


beginFunction = time.time()
linear_search(randomlist, 10)
endFunction = time.time()

begin = time.time()
binary_search(randomlist, 10)
end = time.time()


print("Laufzeit: ", (endFunction-beginFunction) * 1000)
print("Laufzeit: ", (end-begin) * 1000)
