class Shape:
    def area(self):
        return "area not defined"
class Rectangle(Shape):
    def __init__(self, l,b):
        self.l = l
        self.b = b
    def area(self):
        return self.l * self.b
class Circle(Shape):
    def __init__(self, r):
        self.r = r
    def area(self):
        return self.r * 2 * 3.14
circle1 = Circle(4)
print(circle1.area())
rect1 = Rectangle(2,2)
print(rect1.area())
