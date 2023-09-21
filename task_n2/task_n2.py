import math
from task_n2_errors import TriangleDoesNotExistsError, InvalidFigureTypeError

"""
Script that gives figures classes and methods to work with them.
Can be easily added other geometrical primitives by making classes based on Figure class.
Need's only to redefine calc_figure_area method by making correct formula to find new figure's area.
"""


class Figure:
    """Basic figure class. Provides general methods to check correct figure's values."""

    __correct_values_types = (int, float)

    @staticmethod
    def __is_non_negative(number):
        return number >= 0

    @staticmethod
    def __raise_exception_if_incorrect_value():
        raise ValueError

    @classmethod
    def _value_is_correct(cls, value):
        """Check's value for being int or float type and non-negative"""

        is_correct = type(value) in cls.__correct_values_types and cls.__is_non_negative(value)
        return is_correct if is_correct else cls.__raise_exception_if_incorrect_value()

    def calc_figure_area(self, *args):
        """
        Calculate area despite figure type knowing.
        Needs only *args as figure sides.
        Raise error if no correct figure for given variables.
        """

        if len(args) == 1:
            s = Circle(*args).calc_figure_area()
        elif len(args) == 3:
            s = Triangle(*args).calc_figure_area()
        else:
            raise InvalidFigureTypeError
        return s

    def get_figure_variables(self):
        return None


class Circle(Figure):
    """Circle class. Provides methods to calculate figure's area and get object variables"""

    def __init__(self, radius):
        if self._value_is_correct(radius):
            self.__radius = radius
            self.__pi = math.pi
            self.__formula = 'pi * radius^2'

    def calc_figure_area(self):
        s = self.__pi * self.__radius ** 2
        return s

    def get_figure_variables(self):
        answer = f"\nRadius: {self.__radius},\n" \
                 f"Pi: {self.__pi},\n" \
                 f"Formula: {self.__formula}\n"
        return answer


class Triangle(Figure):
    """Triangle class. Provides methods to calculate figure's area and get object variables."""

    def __init__(self, a, b, c):
        if self._value_is_correct(a) and self._value_is_correct(b) and self._value_is_correct(c):
            self.__a = a
            self.__b = b
            self.__c = c
            self.__half_p = (a + b + c) / 2
            self.__formula = 'sqrt(half_p * (half_p - a) * (half_p - b) * (half_p - c))'

    def __is_exists(self):
        """Checks is triangle able to exists with given values."""

        exists = self.__a + self.__b > self.__c and \
            self.__b + self.__c > self.__a and \
            self.__c + self.__a > self.__b
        return exists

    def calc_figure_area(self):
        if self.__is_exists():
            s = math.sqrt(self.__half_p *
                          (self.__half_p - self.__a) *
                          (self.__half_p - self.__b) *
                          (self.__half_p - self.__c))
            return s
        else:
            raise TriangleDoesNotExistsError

    def __is_right(self):
        """
        Check's that triangle is right.
        Triangle is right if:
        Hypotenuse^2 == leg_1^2 + leg_2^2 =>
        Hypotenuse^2 + leg_1^2 + leg_2^2 - hypotenuse^2 == hypotenuse^2 =>
        Sum(powered_triangle_sides) == hypotenuse^2 * 2
        """

        sides = [self.__a, self.__b, self.__c]
        powered_sides = list(map(lambda x: x ** 2, sides))
        return sum(powered_sides) == max(powered_sides) * 2

    def get_figure_variables(self):
        answer = f"\n1-st Side: {self.__a},\n" \
                 f"2-nd Side: {self.__b},\n" \
                 f"3-rd Side: {self.__c}, \n" \
                 f"Formula: {self.__formula}\n" \
                 f"Is exists: {self.__is_exists()}\n"
        if self.__is_right():
            answer += f"Is right: {self.__is_right()}\n"
        return answer


if __name__ == '__main__':

    c1 = Circle(radius=2)
    print(c1.calc_figure_area())
    print(c1.get_figure_variables())

    t1 = Triangle(a=3, b=4, c=5)
    print(t1.calc_figure_area())
    print(t1.get_figure_variables())

    f1 = Figure().calc_figure_area(2)
    f2 = Figure().calc_figure_area(3, 4, 5)
    print(f1)
    print(f2)

    print('Contact me:)\n'
          'https://t.me/artembrshnkv\n')
