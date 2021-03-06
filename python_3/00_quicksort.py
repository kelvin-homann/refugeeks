def quick_sort(start, end, my_list):
    if (start < end):
        p = partition(start, end, my_list)

        quick_sort(start, p - 1, my_list)
        quick_sort(p + 1, end, my_list)


def partition(start, end, my_list):
    pivot_index = start
    pivot = my_list[pivot_index]

    while start < end:
        while start < len(my_list) and my_list[start] <= pivot:
            start += 1

        while my_list[end] > pivot:
            end -= 1

        if (start < end):
            my_list[start], my_list[end] = my_list[end], my_list[start]

    my_list[end], my_list[pivot_index] = my_list[pivot_index], my_list[end]

    return end


if __name__ == "__main__":
    print("Programm is main")
    my_list = [2, 25, 12, 52, 10]
    quick_sort(0, len(my_list) - 1, my_list)
    print(my_list)
