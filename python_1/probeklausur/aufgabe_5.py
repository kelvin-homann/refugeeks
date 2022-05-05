def checkIfListsAreEqual(list1, list2):
    for i in list1:
        if i not in list2:
            return False

    return True


print(checkIfListsAreEqual([1, 2], [1, 3]))  # False
print(checkIfListsAreEqual([5, 6], [5, 6]))  # True
