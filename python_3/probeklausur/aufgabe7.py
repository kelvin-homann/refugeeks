# a)
list = [1, 2, 3]

# Zugriff auf Index ist O(1)
list[1]


# b
list = [1, 2, 3]

# O(n)
for x in list:
    print(x)


# c
list = [1, 2, 3]


# O(n * n) == O(n^2)
for a in list:
    for b in list:
        pass
        # print(a, b)
