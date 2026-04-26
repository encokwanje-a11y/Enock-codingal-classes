import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


# Take input from the user
r = float(input("Enter the radius of the circle: "))

# Create object
c = Circle(r)

# Display results
print("Area of the circle is:", c.area())
print("Perimeter (Circumference) of the circle is:", c.perimeter())