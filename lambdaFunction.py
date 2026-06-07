numbers = [1,2,3,4,5,6,7,8,9]
result = list(map(lambda i: i ** 2,numbers))
print(result)



even_num = list(filter(lambda x: x % 2 == 0,numbers))
print(even_num)



names = ["Yash","Yashika","Yashwant","Yashvi"]
srtd = sorted(names, key=lambda x: len(x), reverse=True)
print(srtd)




# 1write a lambda function that adds 10 to a given numbers:

add_ten = lambda x: x + 10
print(add_ten(5))  # Output: 15



#2 convert a list of string to uppercase
strings = ["hello", "world", "python"]
uppercase_strings = list(map(lambda s: s.upper(), strings))
print(uppercase_strings)  # Output: ['HELLO', 'WORLD', 'PYTHON']




#3 add corresponding element of two list

list1 = [1, 2, 3]
list2 = [4, 5, 6]
added_lists = list(map(lambda x, y: x + y, list1, list2))
print(added_lists)  # Output: [5, 7, 9]



#4 filter names that starts wit "A"



lst = ["Yash","Yashika","Yashwant","Yashvi","Akansha"]
start = list(map(lambda x: x.startswith("A") , lst))
print(start)

#5 5filter out numbers grater than 10

# list = [1,2,4,5,6,7,10,11,12,13]
# greater = list((lambda x: x > 10, list))
# print(greater)  


numbers = [1,2,4,5,6,7,10,11,12,13]

greater = list(filter(lambda x: x > 10, numbers))

print(greater)


#6 write a lambda function that takes two parameter and returns their product
# call the lambda function with the value 5 and 10


product = lambda x, y: x * y
result = product(5, 10)
print(result)  # Output: 50



#7 use a lamda funcrtion to squrre each number in the list [1,2,3,4,5]
numbers = [1,2,3,4,5]
squared = list(map(lambda x: x ** 2, numbers))
print(squared)  # Output: [1, 4, 9, 16, 25]



#8 use lamda function to filter out all even numbers from the lsit[1,2,3,4,5,6,7,8,9]
# print the result

numbers = [1,2,3,4,5,6,7,8,9]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4, 6, 8]

# 9 remove empty strings 

strings = ["hello", "", "world", "", "python"]
non_empty_strings = list(filter(lambda s: s != "", strings))
print(non_empty_strings)  # Output: ['hello', 'world', 'python']



# 10 sort words by length  
words = ["apple", "banana", "kiwi", "grapefruit"]
sorted_words = sorted(words, key=lambda x: len(x))
print(sorted_words)  # Output: ['kiwi', 'apple', 'banana', 'grapefruit']


# 11 Extract last digit each number in the list [23, 45, 67, 89, 12]



numbers = [23, 45, 67, 89, 12] 
laast_digit = list(map(lambda x: x % 10, numbers))
print(laast_digit)  # Output: [3, 5, 7, 9, 2]   



# use a lambda function as the key argument sort a list of tuples based on the second element 
tuples = [(1, 'apple'), (2, 'banana'), (3, 'kiwi')]
sorted_tuples = sorted(tuples, key=lambda x: x[1])
print(sorted_tuples)  # Output: [(1, 'apple'), (2, '