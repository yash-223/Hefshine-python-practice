# 3 write a python program with an abstract class vehicle that has two abstract methods:
# start() and stop().crearte a suclass car that implmentation both methods

from abc import ABC, abstractmethod

class vehicle(ABC):

    @abstractmethod
    def start(self):
        pass
    @abstractmethod
    def stop(self):
        pass
class car(vehicle):
    def start(self):
        return "car is starting"
    def stop(self):
        return "car is stopping"
    
car1 = car()
print(car1.start())
print(car1.stop())


# write an absract class shape with an abstract method draw().which accepts arguments 
# for color and size. implement this method in a subclass cicle.
    



