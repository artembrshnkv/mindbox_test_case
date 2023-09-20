import unittest
from math import pi
from task_n2 import Circle, Triangle


class TestFigures(unittest.TestCase):

    def test_circle_area(self):
        self.assertEqual(Circle(radius=2).calc_figure_area(), pi * 2 ** 2)
        self.assertEqual(Circle(radius=7).calc_figure_area(), pi * 7 ** 2)
        self.assertEqual(Circle(radius=15).calc_figure_area(), pi * 15 ** 2)

    def test_triangle_area(self):
        self.assertEqual(Triangle(a=3, b=4, c=5).calc_figure_area(), 6)
        self.assertEqual(Triangle(a=6, b=5, c=5).calc_figure_area(), 12)
        self.assertEqual(Triangle(a=12, b=16, c=20).calc_figure_area(), 96)
