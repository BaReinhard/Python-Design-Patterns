from animal.animal import Animal


class Dog(Animal):
    """Dog Class inheriting from Animal"""

    def __init__(self, name, legs, spots=0):
        """Constructor methods to call Animal constructor and add new member variables"""
        Animal.__init__(self, name, legs)
        self.spots = spots

    def bark(self):
        """Method to have Dog Speak"""
        return "Woof"
