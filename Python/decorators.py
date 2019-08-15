import functools

def my_decorator(func):
    @functools.wraps(func)
    def function_that_runs_func():
        print("In the decorator!")
        func()
        print("After the decorator!")
    return function_that_runs_func

@my_decorator
def my_function():
    print("Im the function!")

# my_function()

def decorator_with_arguments(number):
    def my_decorator(func):
        @functools.wraps(func)
        def function_that_runs_func(*args, **kwargs):
            print("In the decorator!")
            if number == 56:
                print("Not running the function!")
            else:
                func(*args, **kwargs)
            print("After the decorator!")
        return function_that_runs_func
    return my_decorator

@decorator_with_arguments(526)
def my_function_too(x, y):
    print("Hello")
    print(x)
    print(y)

my_function_too(55, 66)