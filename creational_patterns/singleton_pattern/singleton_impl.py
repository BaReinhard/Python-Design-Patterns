"""Implementation of the Singleton Design Pattern"""
from singleton.singleton import Singleton


# First Create a reference to the Singleton

x = Singleton(HTTP="Headers")
# Add another key value pair to the Singleton
Singleton(AnotherOne="This is another one")
# Print contents
print("Here is the singleton string: \n{}".format(str(x)))
