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

