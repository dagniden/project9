import os

import pytest
from _pytest.capture import CaptureFixture

from src.decorators import log


# def test_log_console(capsys: CaptureFixture[str]) -> None:
#     @log()
#     def my_function(x: int, y: int) -> int:
#         return x + y
#
#     my_function(1, 2)
#     captured = capsys.readouterr()
#     assert "my_function ok\n" in captured.out
#
#
# def test_log_invalid_console(capsys: CaptureFixture[str]) -> None:
#     @log()
#     def func_with_error() -> None:
#         raise ValueError
#
#     with pytest.raises(ValueError):
#         func_with_error()
#
#     captured = capsys.readouterr()
#     assert "func_with_error error: <class 'ValueError'>. Inputs: (), {}\n" in captured.out


def test_log_file() -> None:
    filename = "log.txt"
    current_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(current_dir, "..", "data")
    file_path = os.path.join(data_dir, filename)

    @log(filename)
    def my_test_function(x: int, y: int) -> int:
        return x + y

    my_test_function(1, 2)

    with open(file_path, mode="r") as file:
        data = file.read()

    assert "my_test_function ok" in data


def test_log_invalid_file() -> None:
    filename = "log.txt"
    current_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(current_dir, "..", "data")
    file_path = os.path.join(data_dir, filename)

    @log(filename)
    def func_error1(x: int, y: int) -> int:
        raise TypeError

    with pytest.raises(TypeError):
        func_error1(10, 20)

    with open(file_path, mode="r") as file:
        data = file.read()

    assert "func_error1 error: <class 'TypeError'>. Inputs: (10, 20), {}\n" in data
