import numpy as np

# a
arr = np.array([[1, 2, 3], [4, 5, 6]], np.int32)
print(arr.flatten())
print('------------------------------------------------')
# b
arr = np.array([[[7, 2, 5], [1, 4, 3]], [[9, 5, 3], [6, 8, 2]]], np.int8)
print(arr[1, 1, 2])
print('------------------------------------------------')
# c
arr = np.array([[3 * 2, 4 * 2, 8 * 2], [1 * 1, 3 * 4, 6 * 5]], np.int16)
print(arr.min(), arr.max())
print('------------------------------------------------')
# d
a = np.array([[13, 26]])
b = np.array([[12, 24], [4, 8]])

arr = np.concatenate((a, b), axis=0)
print(arr)
print('------------------------------------------------')
# e
arr = np.array([[1, 2, 3], [4, 5, 6]], np.int8)
print(arr.size, arr.shape)
