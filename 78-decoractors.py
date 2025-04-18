# Decorators super-charge our functions and add extra functionality

# Higher order function HOF, a function that accepts another function
# def greet(func):
#     func()

# or returns another function
# def greet2():
#     def func():
#         return 5
#     return func

def my_decorator(func):
    def wrap_func(*args, **kwargs):
        print('**************')
        func(*args, **kwargs)
        print('**************')
    return wrap_func

@my_decorator
def hello(greeting, emoji=':('):
    print(greeting, emoji)

hello('Hi')


"""
**************
Hi :(
**************
"""
#
# a = my_decorator(hello)
# a('hiiiii', ':)')
#
# @my_decorator
# def bye():
#     print("Bye")
# bye()


# Practical use of decorator

from time import time

def performance(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = fn(*args, **kwargs)
        t2 = time()
        print(
            f"Function {fn.__name__!r} executed in {(t2-t1)*1000} ms")
        return result
    return wrapper


@performance
def long_time():
    for i in range(10000000):
        i * 5

long_time()