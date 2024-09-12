class Vehicle:
    color = "white"
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
class Bus(Vehicle):
    pass
class Car(Vehicle):
    pass
bus = Bus("School Volvo", 180, 12)
car = Car("Audi Q5", 240, 18)
print(f"{bus.color} {bus.name} Speed: {bus.max_speed} Mileage: {bus.mileage}")
print(f"{car.color} {car.name} Speed: {car.max_speed} Mileage: {car.mileage}")
