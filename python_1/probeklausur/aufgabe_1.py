# 1a
a = 10
b = a
b *= 2

print(b)  # 20

# 1b

x = ''
for i in range(10 - 4):
    x += str(i)

print(x)  # 012345

# 1c

my_list = ['x', 'y', 'z']
my_list.append('a')

empty_string = ''
for i in my_list:
    empty_string += i

print(empty_string)  # xyza

# 1d

print(type('a') == str and 3.5 > 1)  # True

# 1e
print("Refugeeks"[0:3])  # Ref
