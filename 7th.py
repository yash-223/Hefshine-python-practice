from abc import ABC, abstractmethod

# create ab abstractmethod class bankAccount with methods deposits() and withdraw
# implement it in savingaccount and currentaccount with different 

class bankAccount(ABC):
    @abstractmethod
    def deposits(self, amount):
        pass
    
    @abstractmethod
    def withdraw(self, amount):
        pass

class savingAccount(bankAccount):
    def deposits(self, amount ):
        return f"Deposited {amount} in saving account"
    
    def withdraw(self, amount):
        return f"Withdrew {amount} from saving account"

class currentAccount(bankAccount):
    def deposits(self, amount):
        



        
        return f"Deposited {amount} in current account"

    def withdraw(self, amount):
        return f"Withdrew {amount} from current account"

here_saving_account = savingAccount()
print(here_saving_account.deposits(1000))


here_current_account = currentAccount()
print(here_current_account.deposits(1000))