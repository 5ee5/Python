class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        self.cars = []

class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def __repr__(self):
        return f"{self.color} {self.brand}"

John = Person("Jonh", 25, "male")

John.cars.append (Car ("BMW", "Black"))
John.cars.append (Car ("Tesla", "White"))

print(f"{John.name}, is {John.age} year old {John.gender}, and own {John.cars}")