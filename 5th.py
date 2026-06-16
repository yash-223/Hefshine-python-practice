# 5 write a python program to calculate the area of different shapes using abstraction 
# what to do:
# 1 create an abstract class shape with an abstract method area().which accepts arguments for color and size. implement this method in a subclass cicle.
# 2 make towo classes inherit from shape class and implement the area method for each shape.
# 3 circle: takes a radius and calculates area using side * side * 3.14
from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def area(self, radius):
        return f"the area of circle is: {3.14 * radius * radius}"

class square(Shape):
    def area(self, side):
        return f"the area of square is: {side * side}"

circle1 = Circle()
print(circle1.area(5))

square1 = square()
print(square1.area(4))
    
