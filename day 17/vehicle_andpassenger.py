# Define two parent classes Vehicle and Passenger with methods drive() and carry_passengers() respectively.
# Then, create a child class called Car that inherits from both Vehicle and Passenger, implementing a method drive_and_carry() that calls both parent methods.
class Vehicle:
    def drive(self):
        print("This is the drive method in class Vehicle")

class Passenger:
    def carry_passengers(self):
        print("This the carry_passengers() method in class Passenger")

class Car(Vehicle,Passenger):
    def drive_and_carry(self):
        self.drive()
        self.carry_passengers()   
        print("drive_and_carry() method running successfully")    
         
example=Car()
example.drive_and_carry()