"""Factory Pattern implemented in Python"""
from factory.factory import get_animal


d = get_animal()
c = get_animal("cow")

print("The Cow goes {}".format(c.moo()))
print("The Dogs goes {}".format(d.bark()))
