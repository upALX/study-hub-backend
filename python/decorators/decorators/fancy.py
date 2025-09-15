def repeat(func):
    def wrapper(func_num: int, *args, **kwargs):
        for _ in range(func_num):
            func(func_num, *args, **kwargs)
    return wrapper

@repeat
def say_hello(func_num: int):
    print("Hello!")

say_hello(4)