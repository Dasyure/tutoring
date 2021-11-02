# def foo(zid=None, name=None, *args, **kwargs):
#     print(zid, name)
#     print(args) # A list
#     print(kwargs) # A dictionary
# if __name__ == '__main__':
#     foo('z3418003', None, 'mercury', 'venus', planet1='earth', planet2='mars')


def make_uppercase(function):
    def wrapper(*args, **kwargs):
        return function(*args, **kwargs).upper()
    return wrapper

@make_uppercase
def get_first_name():
    return "Hayden"

@make_uppercase
def get_last_name():
    return "Smith"

if __name__ == '__main__':
    print(get_first_name())
    print(get_last_name())