import unittest
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        if width < 0 or height < 0:
            raise ValueError("Width and height must be non-negative")
        return self.width * self.height


class TestRectangle(unittest.TestCase):

    def test_calculate_area(self):
        # Test case 1: Positive numbers
        rect1 = Rectangle(5, 10)
        self.assertEqual(rect1.calculate_area(), 50)

        # Test case 2: Zero values
        rect2 = Rectangle(0, 10)
        self.assertEqual(rect2.calculate_area(), 0)

        # Test case 3: Negative numbers
        rect3 = Rectangle(-5, 10)
        self.assertEqual(rect3.calculate_area(), -50)

if __name__ == '__main__':
    unittest.main()        