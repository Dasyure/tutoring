# def echo(*args, **kwargs):
#     for arg in args:
#         print(arg)
#     for kwarg in kwargs:
#         print(kwarg)


# echo("a", "b", name="john", age=10)

def valid_token(function):
    def wrapper(token, *args):
        print(token)
        return function(args)
    return wrapper

@valid_token
def echo(name):
    print(name)

echo("token", "name")