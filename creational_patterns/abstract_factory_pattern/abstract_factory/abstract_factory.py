"""Abstract Factory"""


class Tech(object):
    def __init__(self, chipset="ATMEGA328", ram="16gb", storage="500gb"):
        self._chipset = chipset
        self._ram = ram
        self._storage = storage

    def get_chipset(self):
        """Return Chipset"""
        return self._chipset

    def get_storage(self):
        """Returns Storage Capacity"""
        return self._storage

    def get_ram(self):
        """Returns Ram Capacity"""
        return self._ram


class Computer(Tech):
    """Computer Class"""

    def __init__(self, chipset="ATMEGA328", ram="16gb", storage="500gb"):
        """Calls Parents Constructor"""
        Tech.__init__(self, chipset, ram, storage)

    def __str__(self):
        """Return Str Representation of Class"""
        return "Computer"


class CellPhone(Tech):
    def __init__(self, chipset="INTEL", ram="8gb", storage="256gb"):
        """Calls Parents Constructor"""
        Tech.__init__(self, chipset, ram, storage)

    def __str__(self):
        """Return Str Representation of Class"""

        return "Cell Phone"


class ComputerFactory(object):
    """Returns Computers"""

    def get_tech(self):
        """Return Tech"""
        return Computer()

    def get_price(self):
        """Return Price"""
        return "$700"


class CellFactory(object):
    """ Returns Cell phones"""

    def get_tech(self):
        """Returns Tech"""
        return CellPhone()

    def get_price(self):
        """Returns price"""
        return "$1000"


class BestBuy(object):
    """Store to Return information on products"""

    def __init__(self, tech_factory=None):
        """Set Techfactory"""
        self._tech_factory = tech_factory

    def show_tech(self):
        """Show the Tech in the factory"""
        tech = self._tech_factory.get_tech()
        price = self._tech_factory.get_price()
        print("Our tech is {}".format(tech))
        print("Our tech costs {}".format(price))
        print("Our tech uses the {} chipset, has {} ram and {} storage".format(
            tech.get_chipset(), tech.get_ram(), tech.get_storage()))
