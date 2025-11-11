import unittest
import math

from circle import area as circle_area, perimeter as circle_perimeter
from square import area as square_area, perimeter as square_perimeter
from rectangle import area as rectangle_area, perimeter as rectangle_perimeter
from triangle import area as triangle_area, perimeter as triangle_perimeter

# ====circle.py====
class TestCircle(unittest.TestCase):
    def test_circle_area_zero(self):
        self.assertEqual(circle_area(0), 0)
        
    def test_circle_area_positive(self):
        self.assertAlmostEqual(circle_area(1), math.pi)
        self.assertAlmostEqual(circle_area(3), math.pi * 9)
        self.assertAlmostEqual(circle_area(5), math.pi * 25)
        
    def test_circle_perimeter_zero(self):
        self.assertEqual(circle_perimeter(0), 0)
        
    def test_circle_perimeter_positive(self):
        self.assertAlmostEqual(circle_perimeter(1), 2 * math.pi)
        self.assertAlmostEqual(circle_perimeter(3), 6 * math.pi)
        self.assertAlmostEqual(circle_perimeter(5), 10 * math.pi)

# ====square.py====
class TestSquare(unittest.TestCase):
    def test_square_area_zero(self):
        self.assertEqual(square_area(0), 0)
        
    def test_square_area_positive(self):
        self.assertEqual(square_area(1), 1)
        self.assertEqual(square_area(2), 4)
        self.assertEqual(square_area(5), 25)
        self.assertEqual(square_area(10), 100)
            
    def test_square_perimeter_zero(self):
        self.assertEqual(square_perimeter(0), 0)
        
    def test_square_perimeter_positive(self):
        self.assertEqual(square_perimeter(1), 4)
        self.assertEqual(square_perimeter(3), 12)
        self.assertEqual(square_perimeter(5), 20)
        self.assertEqual(square_perimeter(10), 40)

# ====rectangle.py====
class TestRectangle(unittest.TestCase):
    def test_rectangle_area_zero(self):
        self.assertEqual(rectangle_area(0, 5), 0)
        
    def test_rectangle_area_positive(self):
        self.assertEqual(rectangle_area(1, 1), 1)
        self.assertEqual(rectangle_area(3, 4), 12)
        self.assertEqual(rectangle_area(5, 10), 50)
        self.assertEqual(rectangle_area(7, 3), 21)
        
    def test_rectangle_perimeter_zero(self):
        self.assertEqual(rectangle_perimeter(0, 5), 10)
        
    def test_rectangle_perimeter_positive(self):
        self.assertEqual(rectangle_perimeter(1, 1), 4)
        self.assertEqual(rectangle_perimeter(3, 4), 14)
        self.assertEqual(rectangle_perimeter(5, 10), 30)
        self.assertEqual(rectangle_perimeter(7, 3), 20)

# ====triangle.py====
class TestTriangle(unittest.TestCase):
    def test_triangle_area_zero(self):
        self.assertEqual(triangle_area(0, 5), 0)
        
    def test_triangle_area_positive(self):
        self.assertEqual(triangle_area(1, 1), 0.5)
        self.assertEqual(triangle_area(6, 4), 12)
        self.assertEqual(triangle_area(5, 10), 25)
        self.assertEqual(triangle_area(8, 3), 12)
        
    def test_triangle_perimeter_zero(self):
        self.assertEqual(triangle_perimeter(0, 3, 4), 7)
        
    def test_triangle_perimeter_positive(self):
        self.assertEqual(triangle_perimeter(1, 1, 1), 3)
        self.assertEqual(triangle_perimeter(3, 4, 5), 12)
        self.assertEqual(triangle_perimeter(5, 6, 7), 18)
        self.assertEqual(triangle_perimeter(8, 15, 17), 40)

if __name__ == "__main__":
    unittest.main()