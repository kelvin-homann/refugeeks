str_dict = {"name": "Peter", "hobby": "Fußball"}


def getValuesSum(any_dict):
    sum = 0

    for key in any_dict:
        sum += len(any_dict[key])

    return sum


print(getValuesSum(str_dict))
