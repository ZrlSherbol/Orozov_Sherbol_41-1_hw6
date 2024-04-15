class Figure:
    unit = 'см'

    def __init__(self):
        pass

    def calculate_area(self, width, length):
        return width * length

    def info(self):
        pass

class Circle(Figure):
    def __init__(self, radius):
        super().__init__()
        self.__radius = radius

    def get_radius(self):
        return self.__radius

    def set_radius(self, radius):
        self.__radius = radius

    def calculate_area(self):
        return 3.14159 * self.__radius ** 2

    def info(self):
        area = self.calculate_area()
        print(f"Circle radius: {self.__radius}{self.unit}, area: {area:.2f}{self.unit}.")

class RightTriangle(Figure):
    def __init__(self, side_a, side_b):
        super().__init__()
        self.__side_a = side_a
        self.__side_b = side_b

    def get_side_a(self):
        return self.__side_a

    def set_side_a(self, side_a):
        self.__side_a = side_a

    def get_side_b(self):
        return self.__side_b

    def set_side_b(self, side_b):
        self.__side_b = side_b

    def calculate_area(self):
        return 0.5 * self.__side_a * self.__side_b

    def info(self):
        area = self.calculate_area()
        print(f'RightTriangle side a: {self.__side_a}{self.unit}, side b: {self.__side_b}{self.unit},'
              f' area: {area:.2f}{self.unit}.')

SomeList = [
    Circle(3),
    Circle(5),
    RightTriangle(5, 9),
    RightTriangle(15, 12),
    RightTriangle(72, 54)
]

for i in SomeList:
    i.info()