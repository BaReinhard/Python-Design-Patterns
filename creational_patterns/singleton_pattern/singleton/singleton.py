"""Create Borg and Singleton Class"""


class Borg(object):
    """Borg pattern to create class attributes globally"""
    _shared_state = {}

    def __init__(self):
        self.__dict__ = self._shared_state


class Singleton(Borg):
    """Singleton Class Inheriting a global state from Borg"""

    def __init__(self, **kwargs):
        Borg.__init__(self)
        self._shared_state.update(kwargs)

    def __str__(self):
        return str(self._shared_state)
