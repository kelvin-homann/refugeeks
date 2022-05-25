import random
import time
from bubblesort import bubble_sort
from mergesort import merge_sort
from quicksort import quick_sort


def decideSortingMethod(random_list):
    decision = input("Welcher Algorithmus soll gewählt werden? ")

    if decision == "Mergesort":
        print("Using Mergesort")
        begin = time.time()
        merge_sort(random_list)
        end = time.time()
        print("Laufzeit: {} ms".format((end-begin) * 1000))
    elif decision == "Bubblesort":
        print("Using Bubblesort")
        begin = time.time()
        bubble_sort(random_list)
        end = time.time()
        print("Laufzeit: {} ms".format((end-begin) * 1000))
    elif decision == "Quicksort":
        print("Using Quicksort")
        begin = time.time()
        quick_sort(0, len(random_list) - 1, random_list)
        end = time.time()
        print("Laufzeit: {} ms".format((end-begin) * 1000))


if __name__ == "__main__":
    # my_list = [2, 25, 12, 52, 10]
    my_list = random.sample(range(1, 10000), 9999)
    decideSortingMethod(my_list)
