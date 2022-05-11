class Integer:
    def __init__(self, value) -> None:
        self.value = value

    def add(self, addValue):
        self.value += addValue


my_int = Integer(0)

my_int.add(10)

print(my_int.value)

my_int_list = [Integer(5), Integer(10)]


for i in my_int_list:
    print(i.value)
