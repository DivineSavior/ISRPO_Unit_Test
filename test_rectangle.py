import unittest
import rectangle

class TestRectangle(unittest.TestCase):
    def test_area_positive(self):
        self.assertEqual(rectangle.area(5, 10), 50)
    
    def test_perimeter_positive(self):
        self.assertEqual(rectangle.perimeter(5, 10), 30)
    
    def test_area_zero(self):
        with self.assertRaises(ValueError):
            rectangle.area(0, 5)

if __name__ == '__main__':
    unittest.main()