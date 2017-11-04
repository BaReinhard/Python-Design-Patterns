from decorator.decorator import make_title


@make_title
def hello():
    return "Hello World"


print(hello())
