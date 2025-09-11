import functools
import time


def amount_time(func):
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()
        func_return = func(*args, **kwargs)
        end_time = time.perf_counter()
        print("The final time of execution is: ", end_time - start_time)
        return func_return
    return wrapper_timer

@amount_time
def calculate_something(time: int):

    for t in range(time):
        print(t)

        t +=1


calculate_something(time=1000)