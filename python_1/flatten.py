# Schreibt eine Funktion flatten(list),
# welche eine verschachtelte 2-Dimensionale Liste in eine eindimensionale Liste umwandelt.

def flatten(two_d_list):
    flat_list = []
    for sublist in two_d_list:
        flat_list += sublist
        # for item in sublist:
        #     flat_list.append(item)

    return flat_list


two_d_list = [[24, 23, 1, 32, 2, 3], [29, 64, 4, 1, 9], [29, 64, 4, 1, 9]]

one_d_list = flatten(two_d_list)

print(one_d_list)
