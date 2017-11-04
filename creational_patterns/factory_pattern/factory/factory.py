from dog.dog import Dog
from cow.cow import Cow

"""Create a get_anmial factory to return either a cow or dog"""


def get_animal(animal="dog"):
    animals = dict(dog=Dog("Pluto", 4, 2), cow=Cow("The Cow King", 4, 4))
    return animals[animal]
