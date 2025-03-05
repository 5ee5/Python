import datetime

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age        
        self.cars = []
        print(f"Hey hey I am a new person {self.name}!")

    def __repr__(self):
        return f"{self.name} {self.age}"
    
    def introduce(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

    def add_driving_licence(self, driving_licence):
        if self.age <= 18:
            print(f"{self.name}, you are too young to get a driving licence!")
        else:
            self.driving_licence = driving_licence
            print(f"The driving licence is successfully issued to {self.name}!")


class DrivingLicence:
    def __init__(self, number, category, expiry_date):
        self.number = number
        self.category = category
        self.issue_date = datetime.date
        self.expiry_date = expiry_date


class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def __repr__(self):
        return f"{self.color} {self.brand}"

person1 = Person("Anna", 20)
person2 = Person("Mark", 18)

person1.add_driving_licence(DrivingLicence("LV1234567", "B", "01/01/2028"))

person1.cars = [Car("Volvo", "Black"), Car("Tesla", "White")]
person2.cars = [Car("Subaru", "Blue")]

print(person1.cars)