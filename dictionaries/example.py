keys = ["name", "age", "major"]
values = ["Ivan", 25, "Computer Science"]

student = {}

for i in range(len(keys)):
    key = keys[i]
    value = values[i]
    student[key] = value

print(student)

# OR ------------------------------------------------------------

student = dict(name="Ivan", age=25, major="Computer Science")
print(student)

student = dict([("name", "Ivan"), ("age", 25), ("major", "Computer Science")])
print(student)

# OR -------------------------------------------------------------

keys = ["name", "age", "major"]
values = ["Ivan", 25, "Computer Science"]

student = dict(zip(keys, values))

print(student)

# OR -------------------------------------------------------------

student = {
    "name": "Ivan",
    "age": 25,
    "major": "Computer Science",
}

print(student)
print(student['name'])
print(student.get('name'))

# update value
student['age'] = 27

#  adding key/value if it does not exist
student["address"] = "Sofia"
print(student)

# how to get all keys from a dictionary
for key in student.keys():
    print(key)

# how to change the values by iterating through the keys
numbers = {1: 2, 2: 4, 3: 8}
for key in numbers.keys():
    numbers[key] *= 2
print(numbers)

# adding list in the dictionary
students = {
    "names": ["Ivan", "John"],
    "age": 25,
    "major": "Computer Science",
}

for _ in range(4):
    student_name = input()
    students["names"].append(student_name)
print(students)

# check if a key exists
if "names" in students.keys(): # or: if "names" in students
    print(students["names"])
else:
    print("Error")

# check if a value exists
if 25 in students.values():
    print(students.values())
else:
    print("Error")

# calculate the number of keys:
stock = {"bread": 1, "milk": 3, "cheese": 5}
keys_count = len(stock)

# calculate the number of keys:
stock = {"bread": 1, "milk": 3, "cheese": 5}
values_sum = sum(stock.values())

# print the list keys and values (.items())
stock = {"bread": 1, "milk": 3, "cheese": 5}
for product, quantity in stock.items():
    print(f"{product}: {quantity}")

# clear() removes all elements from a dictionary
stock = {"bread": 1, "milk": 3, "cheese": 5}
stock.clear()
print(stock)

# copy() returns a copy of a dictionary
stock = {"bread": 1, "milk": 3, "cheese": 5}
copied_stock = stock.copy()
print(stock == copied_stock)

# pop() removes and returns an item from a dictionary having the given key
stock = {"fruit": "apple", "vegetable": "cucumber"}
apple = stock.pop("fruit")
print(stock) # {"vegetable": "cucumber"}

# del an item from a dictionary
stocks = {"fruit": "apple", "vegetable": "cucumber"}
del stocks['fruit']
print(stocks) # {"vegetable": "cucumber"}

# popitem() removes an item that was last inserted and returns it as a tuple - (key,value)
stock = {"fruit": "apple", "vegetable": "cucumber"}
print(stock.popitem()) # ("vegetable": "cucumber")
print(stock) # {"fruit": "apple"}

# adding key/value in a dictionary
stock = {"fruit": "apple", "vegetable": "cucumber"}
meat = stock.setdefault('meat', 'chicken')
print(stock) # {"fruit": "apple", "vegetable": "cucumber", "meat", "chicken"}

# .update() adding key/values from other dict into the main dictionary
stock = {"fruit": "apple", "vegetable": "cucumber"}
other_dict = {'others': 'chicken'}
stock.update(other_dict)
print(stock) # {"fruit": "apple", "vegetable": "cucumber", "meat": "chicken", 'others': 'chicken'}
