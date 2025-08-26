import logging
import os
from datetime import datetime
from functools import wraps
from typing import Callable, ParamSpec, TypeVar

P = ParamSpec("P")  # параметры исходной функции
R = TypeVar("R")  # возвращаемое значение исходной функции


def get_logger(log_filename: str) -> logging.Logger:
    """Создает и настраивает отдельный логгер для файла"""
    current_dir = os.path.dirname(os.path.abspath(__file__))
    log_dir = os.path.join(current_dir, "..", "logs")
    os.makedirs(log_dir, exist_ok=True)

    log_file = os.path.join(log_dir, log_filename)

    logger = logging.getLogger(log_filename)  # уникальное имя = имя файла
    logger.setLevel(logging.DEBUG)

    # чтобы не дублировались хендлеры при многократном вызове
    if not logger.handlers:
        file_handler = logging.FileHandler(log_file, encoding="utf-8", mode="w")
        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger


def log(filename: str = "") -> Callable[[Callable[P, R]], Callable[P, R]]:
    """Логирует начало и конец выполнения функции, а также ее результаты или возникшие ошибки"""
    logger = get_logger(filename)

    def decorator(func: Callable[P, R]) -> Callable[P, R]:
        @wraps(func)
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
            start_msg = f"Start {func.__name__} with args={args}, kwargs={kwargs}"
            logger.info(start_msg)

            try:
                result = func(*args, **kwargs)
                logger.info(f"End {func.__name__} → result={result}")
                return result
            except Exception:
                logger.exception(f"Error in {func.__name__}")
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
