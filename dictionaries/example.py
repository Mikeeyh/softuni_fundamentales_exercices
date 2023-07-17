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
