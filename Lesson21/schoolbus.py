# Parent class
class Vehicle:
    def __init__(self, seating_capacity):
        self.seating_capacity = seating_capacity

    def fare(self):
        return self.seating_capacity * 100


# Child class
class Bus(Vehicle):

    # Overriding fare() method
    def fare(self):
        total_fare = super().fare()
        return total_fare + (total_fare * 10 / 100)


# Object creation and output
school_bus = Bus(50)
print("Total Bus Fare is INR", school_bus.fare())