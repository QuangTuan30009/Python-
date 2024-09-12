class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name 
        self.max_speed = max_speed
        self.mileage = mileage
    def display_info(self):
        return f"Vehicle Name: {self.name} Speed: {self.max_speed} Mileage: {self.mileage}"
class Bus(Vehicle):
    def seating_capacity(self, capacity=50):
        return f"The seating capacity of a {self.name} is {capacity} passengers"
bus = Bus("School Vlovo", 180, 12)
print(bus.display_info)
print(bus.seating_capacity())