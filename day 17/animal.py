# Create a Python class called Animal with a method speak() that prints out "Animal speaks". 
# Then, create a subclass called Dog that inherits from Animal and overrides the speak() method to print out "Dog barks".
class Animal:
    def speak(self):
        print("Animal speaks")
class Dog(Animal):
    def speak(self):
        print("Dog barks")
animal=Animal()
dog=Dog()
animal.speak()
dog.speak()
