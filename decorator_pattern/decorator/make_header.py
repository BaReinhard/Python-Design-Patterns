""" Decorator function to wrap function with h1 Tags"""
from functools import wraps


def make_header(func):
    """Wraps func return val in h1 tags"""
    @wraps(func)
    def decorator():
        """Wraps func return val in h1 tags"""
        ret = func()
        return "<h1>" + ret + "</h1>"
    return decorator
