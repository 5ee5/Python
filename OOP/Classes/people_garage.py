class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        self.cars = []
        print(f"I'm a new person: {self.name}!")

    def __repr__(self):
        return f"{self.name} {self.age}"

    def introduce(self):
        print(f"Hello, my name is {self.name} and I'm {self.age} years old")

class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def __repr__(self):
        return f"{self.color} {self.brand}"

# Correct object creation
Anna = Person("Anna", 30, "female")
Anna.introduce()

John = Person("John", 25, "male")

John.cars.append(Car("BMW", "Black"))
John.cars.append(Car("Tesla", "White"))

print(f"{John.name} is a {John.age}-year-old {John.gender}, and owns {John.cars}")

