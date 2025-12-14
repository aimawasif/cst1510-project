class Car:
    """A very simple car class with public attributes"""

    def __init__(self, make, model, year, fuel_type="petrol"):
        self.make = make
        self.model = model
        self.year = year
        self.fuel_type = fuel_type

    def printCar(self):
        print(f"Car Details: {self.make} {self.model} {self.year} {self.fuel_type}")
    def make(self):
        return "Nothing"

# Create a couple of cars (instances)
car1 = Car("Audi", "A3", 2020)
car2 = Car("Volvo", "Xc40", 2021, "electric")

# Access their data using dot notation
car1.printCar()
car2.printCar()
print(car1.make)
print(car1)

class Vehicle:
    """A very simple vehicle class with private attributes"""
    def __init__(self, make, model, year, fuel_type):
        self.make = make
        self.model = model
        self.year = year
        self.fuel_type = fuel_type
    def