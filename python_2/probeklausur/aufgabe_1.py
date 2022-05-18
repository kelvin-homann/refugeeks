# a)
my_dict = {}

my_dict["Name"] = "Max"
print(my_dict)  # {"Name": "Max"}

# # b)
my_tuple = ("Refugeeks", "Python")

my_tuple[1] = "Programming"
print(my_tuple)  # Fehler

# c)
my_dict = {"name": "Max", "alter": 23, "wohnort": "Hannover"}

for i in my_dict.values():
    print(i)  # Max, 23, Hannover

# d)
my_tuple = ("Refugeeks", "Python")

print(my_tuple[1])  # Python

# e)
my_dict = {"name": "Max", "alter": 23, "wohnort": "Hannover"}

del my_dict["wohnort"]
print(my_dict)  # {"name": "Max", "alter": 23}
