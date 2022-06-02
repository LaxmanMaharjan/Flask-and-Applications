from functools import wraps
from timeit import default_timer

def timer(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        start_time = default_timer()
        response = f(*args, **kwargs)
        total_elapsed_time = default_timer() - start_time
        response += f'<h3>Elapsed time: {total_elapsed_time}</h3>'
        return response
    return wrapper
