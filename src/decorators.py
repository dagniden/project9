import os
from functools import wraps


def log(filename: str = ""):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                log_message = f"{func.__name__} ok"
                if filename is "":
                    print(log_message)
                else:
                    write_log(filename, log_message)
                return result
            except Exception as e:
                log_message = f"{func.__name__} error: {type(e)}. Inputs: {args}, {kwargs}"
                if filename is "":
                    print(log_message)
                else:
                    write_log(filename, log_message)
                raise

        return wrapper

    return decorator


def write_log(filename: str, message: str) -> None:
    current_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(current_dir, "..", "data")
    file_path = os.path.join(data_dir, filename)
    os.makedirs(data_dir, exist_ok=True)
    with open(file_path, mode="a", encoding="UTF-8") as file:
        file.write(message + "\n")


if __name__ == "__main__":
    @log()
    def my_function(x, y):
        # return x + y
        raise ValueError("ERROR")


    my_function("abc", 5)
