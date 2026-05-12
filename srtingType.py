str = "Hefshine software"

print(len(str))

print(str.upper())
print(str.lower())
print(str.capitalize())
print(str.title())
print(str.replace("Hefshine", "YAsh"))
print(str.find("e"))
print(str.count("s"))
print(str.strip())
print(str.split())
print(str.startswith("s"))
print(str.endswith("e"))
print(str.isdigit())
print(str.isalpha())
print(str.isspace())
print(str.isalnum())
print(str.isspace())
print(str.istitle())
print(str.islower())

print(str.swapcase())

# Q1
str1 = 'yash sali'
str2 = "It is a doubel qoute"
str3 = """"" its a tripel qoute"""

print(str1 , str2 , str3)



# Q3
print(str1.count("yash"))

# Q4

print(str.isdigit())

# Q5
# print(str1.())

# Q6
a = str1[::-1]
if str1 == a:
    print("its a palindrom")
else:
    print("its palindrom ")

# Q7



# Q8

str = "orange,appel,white,black,green"

splited_str= str.split(",")
sorted_str = sorted(splited_str)
joined_str = ",".join(sorted_str)

print(joined_str)