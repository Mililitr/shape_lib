from math import pi, isclose

class Shape:
    def area(self):
        raise NotImplementedError("area() must be implemented in subclasses")

class Circle(Shape):
    def __init__(self, radius):
        if radius <= 0:
            raise ValueError("Radius must be positive")
        self.radius = radius

    def area(self):
        return pi * self.radius ** 2

class Triangle(Shape):
    def __init__(self, a, b, c):
        if min(a, b, c) <= 0:
            raise ValueError("Triangle sides must be positive")
        # Проверка неравенства треугольника
        if a + b <= c or a + c <= b or b + c <= a:
            raise ValueError("Invalid triangle sides")
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        p = (self.a + self.b + self.c) / 2
        return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5

    def is_right(self):
        # Проверка по теореме Пифагора
        sides = sorted([self.a, self.b, self.c])
        return isclose(sides[2] ** 2, sides[0] ** 2 + sides[1] ** 2, rel_tol=1e-9)

def circle_area(radius):
    return Circle(radius).area()

def triangle_area(a, b, c):
    return Triangle(a, b, c).area()

def create_shape(shape_type, *args):
    """
    Фабричная функция для создания фигур по имени и параметрам.
    shape_type: str ('circle' или 'triangle')
    args: параметры для конструктора фигуры
    """
    if shape_type == "circle":
        return Circle(*args)
    elif shape_type == "triangle":
        return Triangle(*args)
    else:
        raise ValueError(f"Unknown shape type: {shape_type}")