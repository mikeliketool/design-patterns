class Constructor:
    indent_size = 4

    def __str__(self):
        return '\n' + ' ' * self.indent_size + '__init__(self):'


class Field:
    indent_size = 8

    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __str__(self):
        return '\n' + ' ' * self.indent_size + f'self.{self.name} = {self.value}'


class CodeBuilder:
    def __init__(self, class_name):
        self.constructor = Constructor()
        self.code = f'class {class_name}: {self.constructor}'

    def add_field(self, name, value):
        self.code += str(Field(name, value))
        return self

    def __str__(self):
        return self.code


cb = CodeBuilder('Person').add_field('name', '""').add_field('age', '0')
print(cb)
