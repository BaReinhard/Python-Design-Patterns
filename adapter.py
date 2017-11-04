"""Python File Implementing an Adapter Design Pattern"""


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


class Adapter:
    """Adapter Class to simplify other Class Objects unique speak methods"""

    def __init__(self, object_instance, **adapted_method):
        """Constructor methods to create an adapter around an object 
        instances and adapter specific method names given in kwargs"""
        self._object = object_instance
        self.__dict__.update(adapted_method)

    def __getattr__(self, attr):
        """Return other values of object instance as normal"""
        return getattr(self._object, attr)


objects = []
cow = Cow("The Cow King", 4, 3)
dog = Dog("Pluto", 4, 1)
objects.append(Adapter(dog, speak=dog.bark))
objects.append(Adapter(cow, speak=cow.moo))

for obj in objects:
    print("{} says {} and has {} legs and {} spots\n".format(
        obj.name, obj.speak(), obj.legs, obj.spots))
