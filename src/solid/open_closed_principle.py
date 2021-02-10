from enum import Enum


# When addin in new functionality add it by extension and not modification

class Colour(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


class Size(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3


class Product:
    def __init__(self, name, colour, size):
        self.name = name
        self.colour = colour
        self.size = Size


class ProductFilter:
    def filter_by_colour(self, products, colour):
        for p in products:
            if p.colour == colour:
                yield p

    def filter_by_size(self, products, size):
        for p in products:
            if p.size == size:
                yield p
