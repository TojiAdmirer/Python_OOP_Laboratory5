class Vehicle:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def start(self):
        print("Vehicle is starting.")

class Car(Vehicle):
    def start(self):
        print("Car engine is starting.")

v = Vehicle("Subaru", 120)
c = Car("Suzuki", 150)

v.start()
c.start()