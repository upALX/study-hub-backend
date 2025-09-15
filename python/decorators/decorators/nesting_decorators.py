def decorator1(func):
    def wrapper():
        print("Decorator 1 - Antes")
        func()
        print("Decorator 1 - Depois")
    return wrapper

def decorator2(func):
    def wrapper():
        print("Decorator 2 - Antes")
        func()
        print("Decorator 2 - Depois")
    return wrapper

@decorator1
@decorator2
def greet():
    print("Hello!")

greet()
