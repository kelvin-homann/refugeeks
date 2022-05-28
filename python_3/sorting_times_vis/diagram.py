import matplotlib.pyplot as plt
import numpy as np
import time

from mergesort import merge_sort
from bubblesort import bubble_sort
from quicksort import quick_sort


class Diagram:
    def __init__(self):
        self.list_length_steps = [10, 100, 1000, 2000,
                                  3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]

        self.fig, self.axis = plt.subplots()
        self.axis.set(xlabel='Listenlänge (n)', ylabel='Laufzeit (ms)',
                      title='Vergleich von Sortier-Methoden')
        self.axis.set_xticks(self.list_length_steps)

        self.randomListsMergeSort = self.generateRandomLists()
        self.mergeSortTimes = self.measureMergeSortTimes()

        self.randomListsQuickSort = self.generateRandomLists()
        self.quickSortTimes = self.measureQuickSortTimes()

        self.randomListsPythonSort = self.generateRandomLists()
        self.pythonSortTimes = self.measurePythonSortTimes()

        self.randomListsNumpySort = self.generateRandomLists()
        self.numpySortTimes = self.measureNumpySortTimes()

        # self.randomListsBubbleSort = self.generateRandomLists()
        # self.bubbleSortTimes = self.measureBubbleSortTimes()

    def drawLogCurve(self):
        # O(n * log(n))
        x = np.linspace(0, self.bubbleSortTimes[len(
            self.bubbleSortTimes) - 1])
        y = x * np.log(x)

        self.axis.plot(x, y, linewidth=1.0)

    def drawExponentialCurve(self):
        # O(n**2)
        x = np.linspace(0, self.bubbleSortTimes[len(
            self.bubbleSortTimes) - 1])
        y = x * np.exp(2)

        self.axis.plot(x, y, linewidth=1.0)

    def generateRandomLists(self):
        np.random.seed(19680801)
        lists = []

        for i in self.list_length_steps:
            lists.append(np.random.randint(1, 50, size=i).tolist())

        return lists

    def measureMergeSortTimes(self):
        times = []

        for l in self.randomListsMergeSort:
            begin = time.time()
            merge_sort(l)
            end = time.time()
            times.append((end-begin) * 1000)

        return times

    def measureQuickSortTimes(self):
        times = []

        for l in self.randomListsQuickSort:
            begin = time.time()
            quick_sort(0, len(l) - 1, l)
            end = time.time()
            times.append((end-begin) * 1000)

        return times

    def measureBubbleSortTimes(self):
        times = []

        for l in self.randomListsBubbleSort:
            begin = time.time()
            bubble_sort(l)
            end = time.time()
            times.append((end-begin) * 1000)

        return times

    def measurePythonSortTimes(self):
        times = []

        for l in self.randomListsPythonSort:
            begin = time.time()
            l.sort()
            end = time.time()
            times.append((end-begin) * 1000)

        return times

    def measureNumpySortTimes(self):
        times = []

        for l in self.randomListsNumpySort:
            np.asarray(l)  # convert python list to numpy array
            begin = time.time()
            np.sort(l)
            end = time.time()
            times.append((end-begin) * 1000)

        return times

    def drawScatterMergeSort(self):
        self.axis.scatter(self.list_length_steps, self.mergeSortTimes, vmin=0, vmax=self.mergeSortTimes[len(
            self.mergeSortTimes) - 1], c='#d62728', label="Mergesort")

    def drawScatterBubbleSort(self):
        self.axis.scatter(self.list_length_steps, self.bubbleSortTimes, vmin=0, vmax=self.bubbleSortTimes[len(
            self.bubbleSortTimes) - 1], c='#03fc28', label="Bubblesort")

    def drawScatterQuickSort(self):
        self.axis.scatter(self.list_length_steps, self.quickSortTimes, vmin=0, vmax=self.quickSortTimes[len(
            self.quickSortTimes) - 1], c='#032cfc', label="Quicksort")

    def drawScatterPythonSort(self):
        self.axis.scatter(self.list_length_steps, self.pythonSortTimes, vmin=0, vmax=self.pythonSortTimes[len(
            self.pythonSortTimes) - 1], c='#eb9234', label="Python sort()")

    def drawScatterNumpySort(self):
        self.axis.scatter(self.list_length_steps, self.numpySortTimes, vmin=0, vmax=self.numpySortTimes[len(
            self.numpySortTimes) - 1], c='#34ebd2', label="Numpy Sort")

    def draw(self):
        self.drawScatterMergeSort()
        # self.drawScatterBubbleSort()
        self.drawScatterQuickSort()
        self.drawScatterPythonSort()
        self.drawScatterNumpySort()
        # self.drawLogCurve()
        # self.drawExponentialCurve()
        self.axis.legend()
        plt.show()


if __name__ == '__main__':
    diagram = Diagram()
    diagram.draw()
