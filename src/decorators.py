import os
from datetime import datetime
from functools import wraps
from typing import Callable, ParamSpec, TypeVar

P = ParamSpec("P")  # параметры исходной функции
R = TypeVar("R")  # возвращаемое значение исходной функции


def log(filename: str = "") -> Callable[[Callable[P, R]], Callable[P, R]]:
    """Логирует начало и конец выполнения функции, а также ее результаты или возникшие ошибки"""

    def decorator(func: Callable[P, R]) -> Callable[P, R]:
        @wraps(func)
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
            start = get_current_time()
            try:
                result = func(*args, **kwargs)
                stop = get_current_time()
                log_message = f"{start=} {stop=} {func.__name__} ok"
                if filename == "":
                    print(log_message)
                else:
                    write_log(filename, log_message)
                return result
            except Exception as e:
                stop = get_current_time()
                log_message = f"{start=} {stop=} {func.__name__} error: {type(e)}. Inputs: {args}, {kwargs}"
                if filename == "":
                    print(log_message)
                else:
                    write_log(filename, log_message)
                raise

        return wrapper

    return decorator


def get_current_time() -> str:
    """Возвращает текущее время в формате ЧЧ:ММ:СС"""
    return datetime.now().strftime("%H:%M:%S")


def write_log(filename: str, message: str) -> None:
    """Добавляет сообщение в указанный файл в директории data"""
    current_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(current_dir, "..", "data")
    file_path = os.path.join(data_dir, filename)
    os.makedirs(data_dir, exist_ok=True)
    with open(file_path, mode="a", encoding="UTF-8") as file:
        file.write(message + "\n")
