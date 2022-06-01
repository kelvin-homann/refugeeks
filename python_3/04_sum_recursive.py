def recursiveSum(int_list):
    if len(int_list) == 0:
        return 0
    else:
        return int_list[0] + recursiveSum(int_list[1:])


print(recursiveSum([5, 10, 40, 3, 28]))
