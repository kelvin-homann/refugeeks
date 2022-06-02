def recursiveSum(int_list):
    print(int_list)
    if len(int_list) == 1:
        return int_list[0]
    else:
        result = recursiveSum(int_list[1:])
        print(int_list[0], result)
        return int_list[0] * result


print(recursiveSum([5, 10, 40, 3, 28]))
