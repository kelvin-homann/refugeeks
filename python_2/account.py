class Account:
    def __init__(self, name, id, balance):
        self.name = name
        self.id = id
        self.__balance = 0.0

    def __str__(self):
        return str(self.name) + ' ' + str(self.id) + ': ' + str(self.__balance)

    def deposit(self, amount):
        self.__balance = self.__balance + amount

    def getBalance(self, hallo):
        if hallo == "Bilal":
            return self.__balance
        else:
            return None


kelvin = Account("Kelvin", 1, 0)
print(kelvin.getBalance("Bilal"))
