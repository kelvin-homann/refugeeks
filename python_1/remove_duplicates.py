list_with_duplicates = [1, 2, 3, 1, 2, 5, 6, 7, 8]
list_without_duplicates = []

for i in list_with_duplicates:
    if i not in list_without_duplicates:
        list_without_duplicates.append(i)

print(list_without_duplicates)
