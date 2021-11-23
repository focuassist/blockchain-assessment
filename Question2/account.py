import itertools
class Account:
    newId = itertools.count().__next__
    def __init__(self, name, balance):
        self.id = Account.newId()
        self.name = name    
        self.balance = balance

    def deposit(self, amount):
        self.balance+= amount
        print(f"{self.name}'s account deposit {amount}")
        return self.balance

    def withdraw(self, amount):
        if self.balance>=amount:
            self.balance-=amount
            print(f"{self.name}'s account withdraw {amount}")
        else:
            print("\nInsufficient balance  ")

    def __str__(self):
        return f"{self.name}'s account. Balance: {self.balance}"

#Creating a subclass
class Account2(Account):
    @property
    def balance(self):
        print("getter method called")
        return self._balance

    @balance.setter
    def balance(self, amount):
        print("setter method called")
        self._balance = amount

    def transfer(from_account, to_account, amount):
        from_account.withdraw(amount)
        to_account.deposit(amount)

#Test variables
obj1=Account("American Bank", 1000)
obj2=Account2("RHB Bank", 1000)
obj3=Account2("Maybank", 1000)
List =[obj1, obj2]

obj1.deposit(1000)
obj1.withdraw(1000)
obj2.deposit(1000)
Account2.transfer(obj2, obj3, 1000)

# print(vars(obj1))
print(*List, sep="\tnote: ")
print(List.insert(2,obj3))
print(*List, sep="\tnote: ")