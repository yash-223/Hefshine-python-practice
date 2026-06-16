from abc import ABC, abstractmethod
class bankAccount(ABC):
    @abstractmethod
    def deposits(self, amount):
        pass
    
    @abstractmethod
    def withdraw(self, amount):
        pass

class savingAccount(bankAccount):
    def __init__(self):
        self.balance = 0

    def deposits(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance is {self.balance}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance is {self.balance}")
        else:
            print("Insufficient funds")


class currentAccount(bankAccount):
    def __init__(self):
        self.balance = 0
    def deposits(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance is {self.balance}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance is {self.balance}")
        else:
            print("Insufficient funds")

here_saving_account = savingAccount()
here_saving_account.deposits(1000)
here_current_account = currentAccount()
here_current_account.deposits(1000)     
