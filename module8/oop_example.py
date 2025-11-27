from pandas.core.interchange.from_dataframe import primitive_column_to_ndarray
from pandas.core.methods.describe import select_describe_func

from module8.main import perimeter


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width
    def calculate_perimeter(self):
        return 2*(self.length + self.width)

my_rectangle = Rectangle(2, 5)

area = my_rectangle.calculate_area()
perimeter = my_rectangle.calculate_perimeter()

print(f"Area: {area}")
print(f"Perimeter: {perimeter}")
