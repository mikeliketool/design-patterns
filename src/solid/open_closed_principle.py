from enum import Enum


# When addin in new functionality add it by extension and not modification.
# open for extension and closed for modification

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
        self.size = size


# Determines if a particular item satisfies particular criteria
class Specification:
    def is_satisfied(self, item):
        pass

    def __and__(self, other):
        return AndSpecification(self, other)


class AndSpecification(Specification):
    def __init__(self, *items):
        self.items = items

    def is_satisfied(self, item):
        return all(map(
          lambda spec: spec.is_satisfied(item), self.items
        ))


class Filter:
    def filter(self, items, spec):
        pass


class ColourSpecification(Specification):
    def __init__(self, colour):
        self.colour = colour

    def is_satisfied(self, item):
        return item.colour == self.colour


class SizeSpecification(Specification):
    def __init__(self, size):
        self.size = size

    def is_satisfied(self, item):
        return item.size == self.size


class FilterBySpec(Filter):
    def filter(self, items, spec):
        for item in items:
            if spec.is_satisfied(item):
                yield item


if __name__ == '__main__':
    apple = Product('Apple', Colour.GREEN, Size.SMALL)
    tree = Product('Tree', Colour.GREEN, Size.LARGE)
    house = Product('House', Colour.BLUE, Size.LARGE)

    products = [apple, tree, house]

    filter_by_spec = FilterBySpec()
    green = ColourSpecification(Colour.GREEN)

    print('Colour Filter:')
    for product in filter_by_spec.filter(products, green):
        print(f'- {product.name} is green')

    print('Size Filter:')
    large = SizeSpecification(Size.LARGE)
    for product in filter_by_spec.filter(products, large):
        print(f'- {product.name} is large')

    print('Large blue items')
    large_blue = large & ColourSpecification(Colour.BLUE)
    for product in filter_by_spec.filter(products, large_blue):
        print(f'- {product.name} is large and blue')
