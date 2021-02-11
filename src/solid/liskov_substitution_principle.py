# Objects of a superclass shall be replaceable with objects of its subclasses without breaking the application.

class Rectangle:
    def __init__(self, width, height):
        self._height = height
        self._width = width

    @property
    def area(self):
        return self._width * self._height

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._with = value

    def __str__(self):
        return f'width: {self.width}, height: {self.height}'


class Square(Rectangle):
    def __init__(self, size):
        Rectangle.__init__(self, size, size)

    @Rectangle.width.setter
    def width(self, value):
        self._width = self._height = value

    @Rectangle.height.setter
    def height(self, value):
        self._width = self._height = value


def use_it(rc):
    w = rc.width
    rc.height = 10
    expected = int(w * 10)
    print(f'Expected an area of {expected} and got an area of {rc.area}')


rc = Rectangle(2, 3)
use_it(rc)

square = Square(5)
use_it(square)
