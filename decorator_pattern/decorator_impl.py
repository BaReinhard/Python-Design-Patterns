from decorator.make_header import make_header


@make_header
def hello():
    return "Hello World"


print(hello())
