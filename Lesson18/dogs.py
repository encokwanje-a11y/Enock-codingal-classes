# Create Dog class
class Dog:
    animal = "Dog"   # class variable

    def __init__(self, breed, color):
        self.breed = breed
        self.color = color


# Create two objects
dog1 = Dog("Bulldog", "White")
dog2 = Dog("Poodle", "Brown")

# Display details of both dogs
print("First Dog Details")
print("Animal:", Dog.animal)
print("Breed:", dog1.breed)
print("Color:", dog1.color)

print("\nSecond Dog Details")
print("Animal:", Dog.animal)
print("Breed:", dog2.breed)
print("Color:", dog2.color)