def hello_decorator(func):

    def inner1():
        print("this is before function execution")

        func()

        print("this is after function execution")

    return inner1

def used_function():
    print("this is inside the main used function")









used_function = hello_decorator(used_function)
used_function()