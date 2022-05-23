def recursiveSum(int_list):
    if len(int_list) == 1:
        return int_list[0]
    else:
        return int_list[0] + recursiveSum(int_list[1:])


print(recursiveSum([3, 8, 5, 26, 7]))
