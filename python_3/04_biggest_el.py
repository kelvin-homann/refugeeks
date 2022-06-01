def maxElementRecursive(my_list):
    print(my_list)
    if len(my_list) == 1:  # Abbruchbedingung
        return my_list[0]
    else:
        element = maxElementRecursive(my_list[1:])  # Rekursiver Aufruf

        print(element, my_list[0], element > my_list[0])
        if element > my_list[0]:
            return element
        else:
            return my_list[0]


print("Result: ", maxElementRecursive([5, 10, 40, 3, 28]))
