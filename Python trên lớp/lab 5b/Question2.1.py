class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name 
        self.max_speed = max_speed
        self.mileage = mileage
    def display_info(self):
        return f"Vehicle Name: {self.name} Speed: {self.max_speed} Mileage: {self.mileage}"
class bus(Vehicle):
    pass
bus = bus("School Volvo", 180, 12)
print(bus.display_info())
        