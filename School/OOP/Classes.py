class Person:
    def _init_(self, name, age):
        self.name = name
        self.age = age

person1 = Person()
person2 = Person()

person2.name = "Oscar"

print(person1.name)
print(person2.name)
