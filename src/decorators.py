from functools import wraps


def log(filename=None):
    def decorator(func):
        @wraps(func)
        def wrapper(*args):

            try:
                result = func(*args)
                if filename == None:
                    print(f"{func.__name__} ok")

                return result
            except Exception:
                if filename == None:
                    print(f"{func.__name__} error")
            raise Exception

        return wrapper

    return decorator


if __name__ == "__main__":
    @log("1.txt")
    def my_function(x, y):
        return x + y

    my_function(1, 2)