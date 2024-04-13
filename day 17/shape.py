"""Define a parent class Shape with a method draw() that prints out "Shape is being drawn". 
Then, create two child classes Rectangle and Circle that inherit from Shape, 
each overriding the draw() method to print out "Rectangle is being drawn" and "Circle is being drawn" respectively."""
class Shape:
    def draw(self):
        print("Shape is being drawn")
class Rectangle(Shape):
    def draw(self):
        print("Rectangle is being drawn")
class Circle(Shape):
    def draw(self):
        print("Circle is being drawn")
s=Shape()
s.draw()
r=Rectangle()
r.draw()
c=Circle()
c.draw()