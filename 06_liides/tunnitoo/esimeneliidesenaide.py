from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        pass

class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius
    def area(self) -> float:
        return 3.1416 * (self.radius ** 2)

class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height
    def area(self) -> float:
        return self.width * self.height

class Triangle(Shape):
    def __init__(self, base: float, height: float):
        self.base = base
        self.height = height
    def area(self) -> float:
        return (self.base * self.height) / 2

def total_area(shapes: list[Shape]) -> float:
    return sum(shape.area() for shape in shapes)

shapes = [Circle(3), Rectangle(4, 5)]
print(total_area(shapes))

shapes.append(Triangle(6, 4))
print(total_area(shapes))