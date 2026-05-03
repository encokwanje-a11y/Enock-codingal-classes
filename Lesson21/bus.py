class vehicle:
    def __init__(self, name, max_speed, mileage):
        self .name = name
        self .max_speed = max_speed
        self .mileage = mileage
class Bus(vehicle):
            pass
school_bus = Bus("School volvo", 180, 12)
print("vehicle name:", school_bus.name, "speed:", school_bus.max_speed, "Mileage:", school_bus.mileage)
    