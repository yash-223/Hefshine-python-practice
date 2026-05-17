# # a =  int(input("enter a number:"))

# # if a % 2 == 0:
# #     print("even")   
# # else:
# #     print("odd")



# # # check positive or negative

# # a = int(input("enter a number:"))

# # if a > 0:
# #     print("positive")
# # elif a < 0:
# #     print("negative")
# # else:    
# #     print("zero")


# marks = int(input("enter your marks:"))

# if marks >= 90:
#     print("Grad A")
# elif marks >= 80:
#     print("Grad B")
# elif marks >= 70:
#     print("Grad C")
# elif marks >= 60:   
#     print("Grad D")
# elif marks <= 60:
#     print("fail")

# print(marks)

# # find maximu number among three numbers
# a = int(input("enter first number:"))
# b = int(input("enter second number:"))
# c = int(input("enter third number:"))

# if a > b and a > c:
#     print("a is maximum")
# elif b > a and b > c:
#     print("b is maximum")
# elif c > a and c > b:
#     print(f" {c}is maximum")

# print(a)
# print(b)    
# print(c)

# 1.	Write a program to check if a given number is even or odd.
# 2.	Write a program to check if a number is positive, negative, or zero. 
# 3.	Write a program to determine the grade of a student based on their marks.
#              Marks >= 90: Grade A 
#              Marks >= 80: Grade B 
#              Marks >= 70: Grade C 
#              Marks >= 60: Grade D 
#              Marks < 60: Grade F 

# 4.	Write a program to find the maximum of three numbers.
# 5.	Write a program to check if a given year is a leap year. 
# Rules: 
# A year is a leap year if it is divisible by 4 but not divisible by 100 unless it is divisible by 400. 
# Input: A single integer for the year. 
# Output: "Leap Year" or "Not a Leap Year". 

# 6.	Write a program to check if a person is eligible to vote.
# 7.	Write a program that acts as a simple calculator. It should ask the user for two numbers and an operator (+, -, *, /) and perform the corresponding operation. 
# Input: Two integers and a mathematical operator.

# 8.	A student will not be allowed to attend the exam if his/her attendance
# isless than 75%. Take following input from user – 
# Number of classes held  
# Number of classes attended  
# And print on the percentage of class attended Is student is allowed 
# to attend the exam or not.

# 9.	A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years. Ask user for their salary and year of service and print the net bonus amount.
# 10. Write a program to determine the type of triangle based on the  lengths
#  of its three sides. 
# 	All sides equal: "Equilateral" 
# 	Two sides equal: "Isosceles" 
# 	All sides different: "Scalene" 

# Assignments For Students
# 1.	Write a program to check if a number is within the range [10, 50].
# 2.	Write a program to check if a number is divisible by both 3 and 5.
# 3.	Write a program to validate a password. The program should check if the password meets the following conditions: 
# 	At least 8 characters long. 
# 	Contains both uppercase and lowercase letters. 
# 	Contains at least one digit. 
# Input: A string for the password. 
# Output: "Valid Password" or "Invalid Password". 

# 4.	Write a program to print "Fizz" if a number is divisible by 3, "Buzz" if
# divisible by 5, and "FizzBuzz" if divisible by both 3 and 5. Otherwise, print the number itself. 
# Input: A single integer. 
# Output: Fizz, Buzz, FizzBuzz, or the number.

# 5.	Write a code that takes the temperature in Celsius as input and prints out what you should wear:
# •	Below 0°C: "Wear a heavy jacket!"
# •	0°C to 15°C: "Wear a jacket!"
# •	16°C to 25°C: "Wear a t-shirt!"
# •	Above 25°C: "Wear something light!"
# 6.	A shop gives a discount of 10% if the cost of purchased quantity is more than $1000. Take appropriate inputs and print total cost for user. 

# 7.	Write a Python function that calculates the total price of items in a shopping cart and applies a discount based on the total price:
# If the total is greater than $500, apply a 15% discount.
# If the total is between $200 and $500, apply a 10% discount.
# If the total is less than $200, apply no discount.



# Answer--------------------------------------------






# 5.	Write a program to check if a given year is a leap year. 
# Rules: 
# A year is a leap year if it is divisible by 4 but not divisible by 100 unless it is divisible by 400. 
# Input: A single integer for the year. 
# Output: "Leap Year" or "Not a Leap Year". 



# year = int(input("Enter a year: "))

# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print("Leap Year")
# else:
#     print("Not a Leap Year")

#  6.	Write a program to check if a person is eligible to vote.


# age = int(input("enter your age : "))

# if age >= 18:
#     print("enter you can vote")
# else:
#     print("you are not eligible : ")


#  7.	Write a program that acts as a simple calculator. It should ask the user for two numbers and an operator (+, -, *, /) and perform the corresponding operation. 
# # Input: Two integers and a mathematical operator.

# a = int(input("enter a 1st number:"))
# b = int(input("Enter a 2nd number:"))
# operator = input("enter a operator :" )

# if operator == "+":
#     print(a + b)
# elif operator == "-":
#     print(a - b )
# elif operator == "*":
#     print(a*b)
# elif operator == "/":
#     print(a / b)
# else:
#     print("please enter valid operator")



# 8.	A student will not be allowed to attend the exam if his/her attendance
# # isless than 75%. Take following input from user – 
# # Number of classes held  
# # Number of classes attended  
# # And print on the percentage of class attended Is student is allowed 
# # to attend the exam or not.



# name = input("Enter a your name :"  )
# clss =  input("enter your class :")
# attend = int(input("enter your attendance:"))

# if attend <= 75:
#     print(f"{name}  from {clss} you can give exam ")
# else:
#     print("you can not attend exam ")



#  9.	A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years. Ask user for their salary and year of service and print the net bonus amount.

# year = int(input("enter year of experience :"))
# salary = int(input("enter your salry : "))

# if year >= 5:
#     result = (5 / 100 ) * salary
#     print("it is your total increment salry ",result + salary )
#     print("its your 5percent increment ",result)
# else:
#     print("you are not eligible for bounus")













#  10. Write a program to determine the type of triangle based on the  lengths
# #  of its three sides. 
# # 	All sides equal: "Equilateral" 
# # 	Two sides equal: "Isosceles" 
# # 	All sides different: "Scalene" 


a = int(input("Enter a first corner:"))
b = int(input("Enter a second :"))
c = int(input("enter a number :"))

if a == b and a == c and b == a and b == c and c == b and c == a and c == b:
    print("Equilateral")
elif a == b or b == c or a == c:
    print("isosceles")
else:
    print("scalene")




#  3.	Write a program to validate a password. The program should check if the password meets the following conditions: 
# 	At least 8 characters long. 
# 	Contains both uppercase and lowercase letters. 
# 	Contains at least one digit. 
# Input: A string for the password. 
# Output: "Valid Password" or "Invalid Password". 

password = input("Enter password: ")

if len(password) >= 8:
    
    if any(ch.isupper() for ch in password):

        if any(ch.islower() for ch in password):

            if any(ch.isdigit() for ch in password):

                print("Valid Password")

            else:
                print("Invalid Password")

        else:
            print("Invalid Password")

    else:
        print("Invalid Password")

else:
    print("Invalid Password")
















