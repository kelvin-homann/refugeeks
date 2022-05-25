def bubble_sort(my_list):
    n = len(my_list)

    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if my_list[j] > my_list[j + 1]:
                my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
