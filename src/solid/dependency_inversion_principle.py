# High-level modules, which provide complex logic, should be easily reusable and
# unaffected by changes in low-level modules, which provide utility features. To
# achieve that, you need to introduce an abstraction that decouples the high-level
# and low-level modules from each other.
from enum import Enum


class Relationship(Enum):
    PARENT = 0
    CHILD = 1
    SIBLING = 2


class Person:
    def __init__(self, name):
        self.name = name


class Relationships:
    def __init__(self):
        self.relations = []

    def add_parent_and_child(self, parent, child):
        self.relations.append((parent, Relationship.PARENT, child))
        self.relations.append((child, Relationship.CHILD, parent))


class Research:
    def __init__(self, relationships):
        relations = relationships.relations
        for relation in relations:
            if relation[0].name == 'John' and relation[1] == Relationship.PARENT:
                print(f'John has a child called {relation[2].name}')


parent = Person('John')
child1 = Person('Chris')
child2 = Person('Matt')

relationships = Relationships()
relationships.add_parent_and_child(parent, child1)
relationships.add_parent_and_child(parent, child2)

Research(relationships)
