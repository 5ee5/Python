class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.cars = []

class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def __repr__(self):
        return f"{self.color} {self.brand}"

Person.name = "Jolanta"
Person.age = 25
Person.cars = {Car("Volvo", "Black"), Car ("Tesla", "White")}

print(f"{Person.name},is {Person.age} years old, and own {Person.cars}")