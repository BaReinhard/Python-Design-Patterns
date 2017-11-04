"""Python File Implementing an Adapter Design Pattern"""

from dog.dog import Dog
from cow.cow import Cow
from adapter.adapter import Adapter

objects = []
cow = Cow("The Cow King", 4, 3)
dog = Dog("Pluto", 4, 1)
objects.append(Adapter(dog, speak=dog.bark))
objects.append(Adapter(cow, speak=cow.moo))

for obj in objects:
    print("{} says {} and has {} legs and {} spots\n".format(
        obj.name, obj.speak(), obj.legs, obj.spots))
