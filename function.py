# we can store functions in variables, 
def SomeFunction():
    return 10

a = SomeFunction()
print(a) # 10
a = SomeFunction

print(a()) # 10

