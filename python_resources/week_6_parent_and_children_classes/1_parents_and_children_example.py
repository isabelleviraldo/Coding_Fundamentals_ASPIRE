import math

class Shape:
    def __init__(self, sides):
        # store the sides as a list of lengths
        self.sides = sides

    def get_perimeter(self) -> float:
        """Default way to compute perimeter: sum of all sides."""
        return sum(self.sides)


class Rectangle(Shape):
    def __init__(self, w, h):
        # rectangle has 4 sides
        super().__init__([w, h, w, h])
        self.w = w
        self.h = h

    def get_area(self):
        return self.w * self.h


class Circle(Shape):
    def __init__(self, r):
        # perimeter() expects a list of sides; for circle we just use [circumference]
        circumference = 2 * math.pi * r
        super().__init__([circumference])
        self.r = r

    def get_area(self):
        return math.pi * (self.r ** 2)


# test
rect = Rectangle(3, 4)
cir = Circle(2)

print(f"{rect.__class__.__name__}: Perimeter = {rect.get_perimeter():.2f}, Area = {rect.get_area():.2f}")
print(f"{cir.__class__.__name__}: Perimeter = {cir.get_perimeter():.2f}, Area = {cir.get_area():.2f}")
