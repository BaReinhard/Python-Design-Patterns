
""" Adapter Module """


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
