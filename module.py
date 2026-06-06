import calculator
import Area


Area.circle(5)
Area.rectangle(4, 6)    
Area.square(4)




print(calculator.Add(1, 2))
print(calculator.subtract(5, 3))
print(calculator.multiple(4, 6))
print(calculator.divide(10, 2))



# To import specific function from module
# from module_name import fun_names

from calculator import Add
print(Add(1, 2))

# to import all function from module
from calculator import *
print(subtract(5, 3))       # its using run all function
print(multiple(4, 6))
print(divide(10, 2))



# create module Area.py
# Add following function in above module
# circle() , REctangle() , square() , triangle()
#     Each function should calculate and display area of their respective shape. 
