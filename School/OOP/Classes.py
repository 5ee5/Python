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

person1 = Person("Anna", 17)
person2 = Person("Oskars", 18)

person1.name = "Jolanta"
person1.cars = [Car("Volvo", "Black"), Car("Tesla", "White")]
person2.cars = [Car("Subaru", "Blue")]

print(person1.cars)