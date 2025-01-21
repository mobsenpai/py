class Vehicle:
    def __init__(self, type):
        self.type = type
    def display(self):
        print(self.type)
class Car(Vehicle):
    def __init__(self, type, brand, model):
        Vehicle.__init__(self, type)
        self.brand = brand
        self.model = model
    def display(self):
        print(self.type, self.brand, self.model)
class ElectricCar(Car):
    def __init__(self, type, brand, model, battery_cap):
        Car.__init__(self, type, brand, model)
        self.battery_cap = battery_cap
    def display(self):
        print(self.type, self.brand, self.model, self.battery_cap)
car1 = ElectricCar("Car", "Land Rover", "Range Rover", 40)
car1.display()
