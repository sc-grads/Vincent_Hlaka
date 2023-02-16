# exercise 20

# It's time to add a magic method to your class. Consider the Circle class defined below.
# Add a magic method that will automatically be called when printing instances of the class.
# The magic method should only return the radius as a string.
# Then, print the moon object!

# Defining a class
class Circle:
    def __init__(self, radius):    # instance attribute
        self.radius = radius

    # Magic Method that is automatically called when printing an object
    def __str__(self):
        return str(self.radius)     # returning the radius as a string


# Creating an instance called moon with a radius of 1737
moon = Circle(1737)

# Printing the object
print(moon)