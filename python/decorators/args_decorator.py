def decoration_func(func):
    def wrapper(*args, **kwargs):
        print("Hello decorator init")
        func(*args, **kwargs)
        print("Hello decorator end")
        return func(*args, **kwargs)
    return wrapper

@decoration_func
def function_reply(name):
    print(f"Say hello to my little frined: {name}!")
    return name


function_reply("ALX")
