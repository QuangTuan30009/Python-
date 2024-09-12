class Vehicle:
    color = "white"

    def __init__(self, name, max_speed, mileage, seating_capacity):
        self.name = name 
        self.max_speed = max_speed
        self.mileage = mileage
        self.seating_capacity = seating_capacity
    def fare(self):
        return self.seating_capacity * 100
class Bus(Vehicle):
    def __init__(self, name, max_speed, mileage):
        super().__init__(name, max_speed, mileage, seating_capacity=50)

    def fare(self):
        total_fare = super().fare()
        maintenance_charge = total_fare * 0.1
        return total_fare + maintenance_charge
bus = Bus("School Volvo", 180, 12)
print(f"The fare for the bus is: {bus.fare()}")