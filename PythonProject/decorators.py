import time
from functools import wraps


def time_it(func):
    """Decorator that measures the execution time of a function."""

    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()

        execution_time = end_time - start_time
        print(f"[LOG] Function '{func.__name__}' executed in {execution_time:.6f} seconds.")

        return result

    return wrapper