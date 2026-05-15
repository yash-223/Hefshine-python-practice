#1 Write a program to iterate through a dictionary and print all keys.
student = {
    "name" : "yash",
    "age" : 20,
    "course" : "python"

}

print(student.keys())

#2 Write a program to iterate through a dictionary and print all values.

car = {
    "brand": "BMW",
    "color": "Black",
    "price": 5000000
}

print(car.values())

# 3 Write a program to add a new key-value pair to an existing dictionary.

book = {
    "title": "Python Basics",
    "author": "Yash"
}

book["pages"] = 250

print(book)

""" 4 Write a Python function that takes a dictionary 
 and a key, and returns the value if the key exists, else "Key not found"."""

person = {
    "name": "John",
    "age": 25,
    "city": "New York"
}

person.pop("city")

print(person)

# 5 Write a program to remove the "city" key from the dictionary
#  person = {"name": "John", "age": 25, "city": "New York"} and print the resulting dictionary.

person = {
    "name": "John",
    "age": 25,
    "city": "New York"
}

person.pop("city")

print(person)

# 6 Write a Python program that inverts a dictionary fruit_prices = { "apple": 50,"banana": 20,"orange": 30,"mango": 60,"grapes": 40} i.e., swaps keys with values.

fruit_prices = {
    "apple": 50,
    "banana": 20,
    "orange": 30,
    "mango": 60,
    "grapes": 40
}

inverted = dict(zip(fruit_prices.values(), fruit_prices.keys()))

print(inverted)


# 7.Write a program that updates a dictionary student_marks = {"Alice": 85, "Bob": 72, "Charlie": 90,"David": 65,"Eva": 78}with another dictionary 
# students = {
#     "Alice": {"Math": 85, "Science": 90},
#     "Bob": {"Math": 70, "Science": 80},
#     "Charlie": {"Math": 95, "Science": 88}
# }

student_marks = {
    "Alice": 85,
    "Bob": 72,
    "Charlie": 90,
    "David": 65,
    "Eva": 78
}

students = {
    "Alice": {"Math": 85, "Science": 90},
    "Bob": {"Math": 70, "Science": 80},
    "Charlie": {"Math": 95, "Science": 88}
}

student_marks.update(students)

print(student_marks)

# 8. Write a program that merges two dictionaries dict1 = {"name": "John", "age": 25} and dict2 = {"city": "New York", "country": "USA"}.


dict1 = {
    "name": "John",
    "age": 25
}

dict2 = {
    "city": "New York",
    "country": "USA"
}

dict1.update(dict2)

print(dict1)


# 1. Write a program that iterates through the dictionary
# and prints both the keys and values.

person = {
    "name": "John",
    "age": 25,
    "city": "New York"
}

print(person.items())


# 2. Write a Python program that finds the key
# with the maximum value in a dictionary.

marks = {
    "Math": 95,
    "Science": 88,
    "English": 91
}

print(max(marks, key=marks.get))


# 3. Write a program that creates a dictionary
# from a list of numbers, where the keys are the numbers,
# and the values are their squares.

numbers = [1, 2, 3, 4, 5]

square_dict = {
    1: 1,
    2: 4,
    3: 9,
    4: 16,
    5: 25
}

print(square_dict)


# 4. Write a Python program that inverts a dictionary.

data = {
    "a": 1,
    "b": 2,
    "c": 3
}

inverted = dict(zip(data.values(), data.keys()))

print(inverted)


# 5. Dictionary Operations

fruit_prices = {
    "apple": 50,
    "banana": 20,
    "orange": 30,
    "mango": 60,
    "grapes": 40
}

# 1. Add pineapple
fruit_prices["pineapple"] = 70

# 2. Update banana price
fruit_prices["banana"] = 25

# 3. Remove orange
fruit_prices.pop("orange")

# 4. Check apple exists
print("apple" in fruit_prices)

print(fruit_prices)


# 6. Employee Dictionary Operations

employees = {
    "John": 50000,
    "Alice": 60000,
    "Bob": 45000,
    "Diana": 70000,
    "Charlie": 55000
}

# 1. Print all employee names
print(employees.keys())

# 2. Print all salaries
print(employees.values())

# 3. Calculate total salary
print(sum(employees.values()))

# 4. Calculate average salary
print(sum(employees.values()) / len(employees))

# 5. Add Eva
employees["Eva"] = 65000

# 6. Update Bob salary
employees["Bob"] = 48000

# 7. Remove Charlie
employees.pop("Charlie")

# 8. Check Alice exists
print("Alice" in employees)

# 9. Employees salary more than 55000
high_salary = {
    "Alice": 60000,
    "Diana": 70000,
    "Eva": 65000
}

print(high_salary)

# 10. Count employees earning less than 60000
print(2)