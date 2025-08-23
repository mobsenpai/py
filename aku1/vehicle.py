class Vehicle():
    def __init__(self, type):
        self.type = type

class Car(Vehicle):
    def __init__(self, type, brand, model):
        Vehicle.__init__(self, type)
        self.brand = brand
        self.model = model

class ElectricCar(Vehicle, Car):
    def __init__(self, type, brand ,model, battery):
        Car.__init__(self, type, brand, model)
        self.battery = battery

