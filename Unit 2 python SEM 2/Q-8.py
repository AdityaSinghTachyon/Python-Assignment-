# Create a base class Vehicle with a method move() and two subclasses Car and Bicycle. Override the move() method in both subclasses. The Car should print "Driving on the road". Demonstrate polymorphism by calling the move() method on both objects.

# Base class
class Vehicle:
    def move(self):
        print("The vehicle is moving")

# Subclass Car
class Car(Vehicle):
    def move(self):
        print("Driving on the road")

# Subclass Bicycle
class Bicycle(Vehicle):
    def move(self):
        print("Pedaling on the road")

# Demonstrating polymorphism
vehicles = [Car(), Bicycle()]

for v in vehicles:
    v.move()