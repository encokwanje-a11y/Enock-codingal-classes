# Create Dog class
class Dog:
    # Class variable
    animal = "Dog"

    # Constructor
    def __init__(self, breed, color):
        self.breed = breed
        self.color = color

    # Method to display details
    def display_details(self):
        print("Animal:", Dog.animal)
        print("Breed:", self.breed)
        print("Color:", self.color)
        print("---------------------")


# Create objects for different dog breeds
dog1 = Dog("German Shepherd", "Black and Tan")
dog2 = Dog("Labrador Retriever", "Golden")

# Display details of both dogs
dog1.display_details()
dog2.display_details()