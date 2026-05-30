# try:

#     a = int(input("Enter a "))
#     b = int(input("Enet b"))
#     c = a/b
#     print("Division",c)
# except:
#     print("its not divisible by Zero!!!!")


     

# # multiple except statetement:

# try:
#    a = int(input("Enter a "))
#    b = int(input("Enet b"))

#    c = a/b
#    print("Division",c)

# except ZeroDivisionError:
#     print("can not divode by zero!!!!!") 
# except ValueError:
#     print("its a ValuError!!!!")     # if showing valueError that time execute valueerror
# else:
#     print("Else block executed!!!!!!!")      # if try box is not execute 
# finally:
#     print("Finally block executed!!!!!!!")  # any time run 


# using Exception class 

try:
   a = int(input("Enter a "))
   b = int(input("Enet b"))

   c = a/b
   
  

except Exception as e:
    print(e) 

else:
    print("Else block executed!!!!!!!")      # if try box is not execute 
finally:
    print("Finally block executed!!!!!!!")  # any time run 