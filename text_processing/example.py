# How to print single '\':
message = "C:\\path\\to\\file"
print(message) # C:\path\to\file

# How to print more than one quotation marks:
print("I\'m happy")
print("He said \"Hello!\"")

# How to print words separated horizontally:
message = "Hello\tWorld"
print(message) # Hello   World

# How to write multi-line string
message = """This is randon text
row 2 - test
row 3 - test
"""
print(message) # prints the message in 3 lines

# concatenation
str1 = "Hello"
str2 = "World"
print(str1 + str2) # prints Hello World
print(str1 * 10) # prints 10 times Hello

# formatting with %
x = "apples"
y = "lemons"
z = "In the basket are %s and %s" % (x, y)
print(z) # prints In the basket are apples and lemons

name = "Mike"
age = 25
z = "My name is %s and I am %d years old" % (name, age)
print(z) # prints My name is Mike and I am 25 years old

# formatting with {}
x = "apples"
y = "lemons"
z = "In the basket are {} and {}".format(x, y)
print(z) # prints In the basket are apples and lemons

name = "Mike"
age = 25
z = "My name is {} and I am {} years old".format(name, age)
print(z) # prints My name is Mike and I am 25 years old

price = 12.34
quantity = 5
total = "The total cost is ${:.2f} for {} items.".format(price * quantity, quantity)
print(total)

# slicing

text = "My name is Peter"
name = text[-5:] # or text[11:]
print(name) # prints Peter

text = "This is SoftUni Fundamentals"
course = text[slice(16, len(text))] # to slice from 16th element to the last one which is equals to the length of the str
print(course) # prints Fundamentals

# METHODS ---------------------------------------------------

'1'.isdigit() # True
'p'.isdigit() # False
'P'.isupper() # True
'P'.islower() # False
'u'.islower() # True
"hello".upper() # "HELLO"
"HeLLo".lower() # "hello"
" Mike ".lstrip() # "Mike "
" Mike ".rstrip() # " Mike"
" Mike ".strip() # "Mike"

string = "hello world"
print(string.capitalize())

text = "Hello World"
print(text.casefold())

# count of some element
text = "hello world"
print(text.count('o')) # 2, because there are two times 'o' in the text

# endswith /// startswith() - The same as 'endswith' but the opposite of it.
text = 'Mike'
print(text.endswith('ke')) # gives us True because the text ends with 'ke'

# How to print the index of some letter of the string
string = "Hello World"
print(string.index('o')) # gives us the index of the first 'o'
print(string.index('o', 5)) # gives the index of the 'o', but it is searching from the 5th index to the end
print(string.find('o')) # = string.idex(), but gives us '-1' if the letter does not exist



