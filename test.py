import unittest
from area import Circle, Triangle, circle_area, triangle_area, create_shape, Shape

class TestAreaLibrary(unittest.TestCase):
    def test_circle_area(self):
        self.assertAlmostEqual(circle_area(1), 3.141592653589793)
        self.assertAlmostEqual(Circle(2).area(), 12.566370614359172)

    def test_triangle_area(self):
        self.assertAlmostEqual(triangle_area(3, 4, 5), 6.0)
        self.assertAlmostEqual(Triangle(5, 12, 13).area(), 30.0)

    def test_circle_invalid(self):
        with self.assertRaises(ValueError):
            Circle(0)
        with self.assertRaises(ValueError):
            Circle(-1)

    def test_triangle_invalid(self):
        with self.assertRaises(ValueError):
            Triangle(1, 2, 3)
        with self.assertRaises(ValueError):
            Triangle(-1, 2, 2)
        with self.assertRaises(ValueError):
            Triangle(0, 2, 2)

    def test_triangle_is_right(self):
        self.assertTrue(Triangle(3, 4, 5).is_right())
        self.assertTrue(Triangle(5, 12, 13).is_right())
        self.assertFalse(Triangle(3, 4, 6).is_right())

    def test_create_shape(self):
        c = create_shape("circle", 3)
        t = create_shape("triangle", 3, 4, 5)
        self.assertIsInstance(c, Circle)
        self.assertIsInstance(t, Triangle)
        self.assertAlmostEqual(c.area(), circle_area(3))
        self.assertAlmostEqual(t.area(), triangle_area(3, 4, 5))
        with self.assertRaises(ValueError):
            create_shape("square", 2)

    def test_polymorphism(self):
        shapes = [Circle(2), Triangle(3, 4, 5)]
        areas = [shape.area() for shape in shapes]
        self.assertAlmostEqual(areas[0], circle_area(2))
        self.assertAlmostEqual(areas[1], triangle_area(3, 4, 5))

    def test_extensibility(self):
        class Rectangle(Shape):
            def __init__(self, a, b):
                self.a = a
                self.b = b
            def area(self):
                return self.a * self.b
        r = Rectangle(2, 3)
        self.assertEqual(r.area(), 6)

if __name__ == "__main__":
    unittest.main()