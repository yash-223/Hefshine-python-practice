from abc import ABC, abstractmethod

class employee(ABC):
    @abstractmethod
    def salary(self):
        pass
# part time and fulltime
class parttime(employee):
    def salary(self, ):
        return f"the salary of part time employee is: {hours * rate}"
    
class fulltime(employee):
    def salary(self, hours, rate):
        return f"the salary of full time employee is: {hours * rate}"
    
parttime1 = parttime()
print(parttime1.salary(20, 100))

fulltime1 = fulltime()
print(fulltime1.salary(40, 200))


# create ab abstractmethod class bankAccount with methods deposits() and withdraw
# implement it in savingaccount and currentaccount with different 




