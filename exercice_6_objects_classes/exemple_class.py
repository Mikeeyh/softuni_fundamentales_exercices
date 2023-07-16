class Person:
    def __init__(self, name, last_name):
        self.name = name
        self.last_name = last_name

    def greeting_by_name(self):
        return f"Hello {self.name}"


name = "Mike"
last_name = "Haralanov"
person = Person(name, last_name)
person1 = Person("Kalin", "Petrov")

print(person.name)
print(person.last_name)

person.name = "Ivan"   # changing the name // if we update the attribute to _name (private attribute), cannot be changed

print(person.name)
print(person.greeting_by_name())

print(person1.greeting_by_name())

