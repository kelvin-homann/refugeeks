my_list = [5, 3, 12, 2, 8]


def sumOfListElement(int_list):
    sum = 0
    for i in int_list:
        sum += i

    return sum


print(sumOfListElement(my_list))
