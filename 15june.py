from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def speak(self):
        pass

    @abstractmethod
    def movement(self):
        pass
class Dog(Animal):
    def speak(self):
        return "Bark...! "
    
    def movement(self):
        return "running"
    
class fish(Animal):
    def speak(self):
        return "blub "
    
    def movement(self):
        return "swim"
    
dog1 = Dog()
print(dog1.speak())
print(dog1.movement())
fish1 = fish()
print(fish1.speak())
print(fish1.movement())



    

