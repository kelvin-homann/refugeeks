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
                      title='BubbleSort vs Mergesort')
        self.axis.set_xticks(self.list_length_steps)

        self.randomListsMergeSort = self.generateRandomLists()
        self.randomListsBubbleSort = self.generateRandomLists()
        self.randomListsQuickSort = self.generateRandomLists()

        self.mergeSortTimes = self.measureMergeSortTimes()
        self.quickSortTimes = self.measureQuickSortTimes()
        self.bubbleSortTimes = self.measureBubbleSortTimes()
        # self.ax.set_yticks(self.bubbleSortTimes)

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

    def drawScatterMergeSort(self):
        self.axis.scatter(self.list_length_steps, self.mergeSortTimes, vmin=0, vmax=self.mergeSortTimes[len(
            self.mergeSortTimes) - 1], c='#d62728', label="Mergesort")

    def drawScatterBubbleSort(self):
        self.axis.scatter(self.list_length_steps, self.bubbleSortTimes, vmin=0, vmax=self.bubbleSortTimes[len(
            self.bubbleSortTimes) - 1], c='#03fc28', label="Bubblesort")

    def drawScatterQuickSort(self):
        self.axis.scatter(self.list_length_steps, self.quickSortTimes, vmin=0, vmax=self.quickSortTimes[len(
            self.quickSortTimes) - 1], c='#032cfc', label="Quicksort")

    def draw(self):
        self.drawScatterMergeSort()
        self.drawScatterBubbleSort()
        self.drawScatterQuickSort()
        # self.drawLogCurve()
        # self.drawExponentialCurve()
        self.axis.legend()
        # plt.xlim(0, self.bubbleSortTimes[0])
        plt.show()


if __name__ == '__main__':
    diagram = Diagram()
    diagram.draw()
