# Decorator - Its design pattern that allows to modify the functionality of a function by wrapping it  another function
# decorator is called before calling original function
# There are two ways to use a Decorator as follows

# 1st way
def my_decorator(func):
    print("in decorator function")

    def wrapper(a,b):
        print("in inner function")
        if b == 0:
            print("b value is 0")
        else:
            func(a, b)
    return wrapper


@my_decorator
def divide(a, b):
    print("inside divide function")
    result = a/b
    print(result)


divide(10,2)
divide(10,0)


# 2st way
def my_decorator(func):
    def wrapper(name):
        print("Before calling function")
        if name == "pankaj":
            func(name)
        else:
            print("name is not pankaj")
        print("After calling function")
    return wrapper


def say_hello(name):
    print(f"from function hello {name}")


var1 = my_decorator(say_hello)
var1("pankaj")
