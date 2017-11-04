from functools import wraps


def make_title(func):
    @wraps(func)
    def decorator():
        ret = func()
        return "<h1>" + ret + "</h1>"
    return decorator
