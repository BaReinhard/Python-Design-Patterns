class Animal(object):
    """Animal Base Class"""

    def __init__(self, name="Animal", legs=0):
        self.name = name
        self.legs = legs


class Cow(Animal):
    """Cow Class inheriting from Animal"""

    def __init__(self, name, legs, spots=0):
        """Constructor methods to call Animal constructor and add new member variables"""
        Animal.__init__(self, name, legs)
        self.spots = spots

    def moo(self):
        """Method to have cow speak"""
        return "Moo"


class Dog(Animal):
    """Dog Class inheriting from Animal"""

    def __init__(self, name, legs, spots=0):
        """Constructor methods to call Animal constructor and add new member variables"""
        Animal.__init__(self, name, legs)
        self.spots = spots

    def bark(self):
        """Method to have Dog Speak"""
        return "Woof"


def get_animal(animal="dog"):
    animals = dict(dog=Dog("Pluto", 4, 2), cow=Cow("The Cow King", 4, 4))
    return animals[animal]
