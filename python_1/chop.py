def middle(list):
    list.pop(0)
    list.pop()
    return list


listone = [1, 2, 3, 4, 5, 6]
listtwo = [2, 3, 1, 5, 4, 6]
listone_short = middle(listone)
print(listone_short)
listtwo_short = middle(listtwo)
print(listtwo_short)
