# Polymorphism Example

class BMW:
    def fuel_type(self):
        print("Fuel Type: Petrol")

    def max_speed(self):
        print("Max Speed: 250 km/h")


class Ferrari:
    def fuel_type(self):
        print("Fuel Type: Petrol")

    def max_speed(self):
        print("Max Speed: 340 km/h")


# Function demonstrating polymorphism
def car_details(car):
    car.fuel_type()
    car.max_speed()
    print()


# Creating objects
bmw = BMW()
ferrari = Ferrari()

# Using the same function for different objects
car_details(bmw)
car_details(ferrari)